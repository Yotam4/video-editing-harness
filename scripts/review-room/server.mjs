// Adapted from talsiach/take-one at 43fd27b8878241deb50a5884a154b173272b858f.
// Copyright (c) 2026 Tal Siach. MIT; see ../../licenses/take-one-MIT.txt.
// Local cut comparison and frame notes. No upload or messaging service is used.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const fail = (message, status = 400) => Object.assign(new Error(message), { status });
const json = (response, status, value) => {
  response.writeHead(status, { 'content-type': 'application/json', 'cache-control': 'no-store' });
  response.end(JSON.stringify(value));
};

async function readBody(request) {
  const chunks = [];
  let bytes = 0;
  for await (const chunk of request) {
    bytes += chunk.length;
    if (bytes > 4 * 1024 * 1024) throw fail('Note is too large', 413);
    chunks.push(chunk);
  }
  try { return JSON.parse(Buffer.concat(chunks).toString() || '{}'); }
  catch { throw fail('Invalid JSON'); }
}

function sendFile(request, response, filename, type) {
  if (!fs.existsSync(filename)) throw fail('File not found', 404);
  const size = fs.statSync(filename).size;
  const headers = { 'content-type': type, 'accept-ranges': 'bytes', 'cache-control': 'no-store' };
  let start = 0, end = size - 1, status = 200;
  if (request.headers.range) {
    const match = /^bytes=(\d*)-(\d*)$/.exec(request.headers.range);
    if (!match || (!match[1] && !match[2])) throw fail('Invalid byte range', 416);
    start = match[1] ? Number(match[1]) : Math.max(0, size - Number(match[2]));
    end = match[1] && match[2] ? Math.min(Number(match[2]), size - 1) : size - 1;
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start < 0 || start > end || start >= size) {
      response.writeHead(416, { 'content-range': `bytes */${size}` });
      return response.end();
    }
    headers['content-range'] = `bytes ${start}-${end}/${size}`;
    status = 206;
  }
  response.writeHead(status, { ...headers, 'content-length': end - start + 1 });
  if (request.method === 'HEAD') return response.end();
  const stream = fs.createReadStream(filename, { start, end });
  stream.on('error', () => response.destroy());
  stream.pipe(response);
}

export function createReviewServer(folder) {
  const root = fs.realpathSync(folder);
  const directory = path.join(root, 'review-notes');
  const shots = path.join(directory, 'shots');
  const notesFile = path.join(directory, 'notes.json');
  const cache = new Map();
  fs.mkdirSync(shots, { recursive: true });
  const load = () => fs.existsSync(notesFile) ? JSON.parse(fs.readFileSync(notesFile, 'utf8')) : { notes: [], sent: [] };
  const save = (data) => {
    const temporary = notesFile + '.tmp';
    fs.writeFileSync(temporary, JSON.stringify(data, null, 2) + '\n');
    fs.renameSync(temporary, notesFile);
  };
  async function cuts() {
    const output = [];
    for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
      if (!entry.isFile() || !/\.mp4$/i.test(entry.name)) continue;
      const filename = path.join(root, entry.name), stat = fs.statSync(filename);
      const key = `${stat.mtimeMs}:${stat.size}`;
      if (cache.get(entry.name)?.key !== key) {
        const probe = spawnSync('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_frames',
          '-show_entries', 'frame=best_effort_timestamp_time', '-of', 'json', filename], { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
        if (probe.error || probe.status !== 0) throw fail(`Cannot inspect ${entry.name}`, 422);
        const stamps = JSON.parse(probe.stdout).frames.map((frame) => Number(frame.best_effort_timestamp_time));
        const times = stamps.map((time) => time - stamps[0]);
        if (!times.length || times.some((time, i) => !Number.isFinite(time) || (i && time < times[i - 1]))) {
          throw fail(`Invalid frame times in ${entry.name}`, 422);
        }
        const hash = crypto.createHash('sha256');
        for await (const chunk of fs.createReadStream(filename)) hash.update(chunk);
        cache.set(entry.name, { key, name: entry.name, mtime: stat.mtimeMs, sha256: hash.digest('hex'), frame_times: times });
      }
      const { key: ignored, ...cut } = cache.get(entry.name);
      output.push(cut);
    }
    return output.sort((a, b) => b.mtime - a.mtime);
  }
  return http.createServer(async (request, response) => {
    try {
      const host = String(request.headers.host || ''), origin = request.headers.origin;
      if (!/^(localhost|127\.0\.0\.1):\d+$/.test(host) || (origin && origin !== 'http://' + host)) {
        throw fail('Forbidden origin', 403);
      }
      const route = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
      const reading = request.method === 'GET' || request.method === 'HEAD';
      if (route === '/' && reading) return sendFile(request, response, path.join(HERE, 'index.html'), 'text/html; charset=utf-8');
      if (route === '/api/cuts' && reading) return json(response, 200, await cuts());
      if (route.startsWith('/video/') && reading) {
        const name = route.slice('/video/'.length);
        if (!(await cuts()).some((cut) => cut.name === name)) throw fail('Cut not found', 404);
        return sendFile(request, response, path.join(root, name), 'video/mp4');
      }
      if (/^\/shots\/[a-f0-9-]+\.jpg$/.test(route) && reading) {
        return sendFile(request, response, path.join(shots, path.basename(route)), 'image/jpeg');
      }
      if (route === '/api/notes' && reading) return json(response, 200, load());
      if (route === '/api/notes' && request.method === 'POST') {
        const body = await readBody(request);
        const cut = (await cuts()).find((value) => value.name === body.cut);
        if (!cut || body.cut_sha256 !== cut.sha256) throw fail('Cut version changed; reload before adding a note', 409);
        if (typeof body.text !== 'string' || !body.text.trim() || body.text.length > 4000) throw fail('Use 1–4000 characters');
        let frame = null;
        if (body.t !== undefined) {
          if (!Number.isFinite(body.t) || body.t < 0 || body.t > cut.frame_times.at(-1) + 0.0001) throw fail('Time is outside the cut');
          frame = cut.frame_times.findLastIndex((time) => time <= body.t + 0.000001);
        }
        const pinned = body.x !== undefined || body.y !== undefined;
        if (pinned && (frame === null || ![body.x, body.y].every((value) => Number.isFinite(value) && value >= 0 && value <= 1))) {
          throw fail('A pin needs a frame and coordinates between 0 and 1');
        }
        const note = { id: crypto.randomUUID(), cut: cut.name, cut_sha256: cut.sha256,
          t: frame === null ? null : cut.frame_times[frame], frame,
          x: pinned ? body.x : null, y: pinned ? body.y : null,
          text: body.text, at: new Date().toISOString(), done: false };
        if (typeof body.shot === 'string' && body.shot.startsWith('data:image/jpeg;base64,')) {
          fs.writeFileSync(path.join(shots, note.id + '.jpg'), Buffer.from(body.shot.slice(23), 'base64'));
          note.shot = 'shots/' + note.id + '.jpg';
        }
        const data = load(); data.notes.push(note); save(data);
        return json(response, 201, note);
      }
      const match = /^\/api\/notes\/([a-f0-9-]+)$/.exec(route);
      if (match && request.method === 'POST') {
        const body = await readBody(request), available = await cuts(), data = load();
        const note = data.notes.find((value) => value.id === match[1]);
        if (!note) throw fail('Note not found', 404);
        if (typeof body.done !== 'boolean') throw fail('Expected done: true or false');
        if (body.done) {
          const replacement = available.find((cut) => cut.name === body.resolved_in);
          if (!replacement || replacement.sha256 === note.cut_sha256) throw fail('Choose the revised comparison cut before marking done');
          note.resolved_in = { cut: replacement.name, sha256: replacement.sha256 };
        } else { delete note.resolved_in; }
        note.done = body.done; save(data); return json(response, 200, note);
      }
      if (match && request.method === 'DELETE') {
        const data = load(); data.notes = data.notes.filter((note) => note.id !== match[1]); save(data);
        fs.rmSync(path.join(shots, match[1] + '.jpg'), { force: true });
        return json(response, 200, { ok: true });
      }
      if (route === '/api/send' && request.method === 'POST') {
        const body = await readBody(request), data = load();
        if (!(await cuts()).some((cut) => cut.name === body.cut)) throw fail('Cut not found', 404);
        const batch = { at: new Date().toISOString(), cut: body.cut, open: data.notes.filter((note) => !note.done && note.cut === body.cut).length };
        data.sent.push(batch); save(data);
        fs.appendFileSync(path.join(directory, 'sent.log'), JSON.stringify(batch) + '\n');
        return json(response, 200, { ok: true, message: 'Notes saved locally; no message was sent' });
      }
      throw fail('Not found', 404);
    } catch (error) {
      if (!response.headersSent) json(response, error.status || 500, { error: error.message });
      else response.destroy();
    }
  });
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (!process.argv[2]) { console.error('Usage: node scripts/review-room/server.mjs <cuts-folder> [port=4400]'); process.exit(1); }
  const port = Number(process.argv[3] || 4400);
  const server = createReviewServer(process.argv[2]);
  server.on('error', (error) => { console.error(error.message); process.exitCode = 1; });
  server.listen(port, '127.0.0.1', () => console.log(`Ela Maayan review room: http://127.0.0.1:${server.address().port}`));
}
