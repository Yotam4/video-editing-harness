#!/usr/bin/env python3
"""Summarize one publication-level snapshot; do not infer unique account totals."""
import argparse, csv, json, statistics
from collections import Counter

def numeric(row, key):
    value = row.get(key)
    return None if value in (None, "") else float(value)

def summarize(rows, min_reach=100):
    ids = [r["post_id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate publication IDs; reconcile before comparing")
    result = {"rows": len(rows), "formats": dict(Counter(r["format"] for r in rows)), "groups": {}}
    for group in sorted({r["format"] + "/" + r["theme"] for r in rows} | {"all_reels"}):
        selected = [r for r in rows if (r["format"] + "/" + r["theme"] == group if group != "all_reels" else r["format"] == "reel")]
        eligible = [r for r in selected if (numeric(r, "reach") or 0) >= min_reach]
        values = {"rows": len(selected), "eligible_rows": len(eligible), "min_reach": min_reach}
        for key in ["reach", "watch_seconds", "view_rate_3s_pct"]:
            a = [numeric(r,key) for r in eligible if numeric(r,key) is not None]
            values["median_" + key] = statistics.median(a) if a else None
        for key in ["shares", "saves", "follows"]:
            a = [100 * numeric(r,key) / numeric(r,"reach") for r in eligible if numeric(r,key) is not None]
            values["median_" + key + "_per_100_reached"] = statistics.median(a) if a else None
        result["groups"][group] = values
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--min-reach", type=float, default=100)
    args = parser.parse_args()
    if args.min_reach <= 0:
        parser.error("--min-reach must be positive")
    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        print(json.dumps(summarize(list(csv.DictReader(handle)), args.min_reach), ensure_ascii=False, indent=2))
