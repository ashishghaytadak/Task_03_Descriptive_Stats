#!/usr/bin/env python3


import argparse
import os

import pandas as pd

_BASE = ["", "na", "n/a", "nan", "null", "none"]
NA_VALUES = sorted({t for b in _BASE for t in (b, b.upper(), b.title())})


def load(path):
    return pd.read_csv(path, na_values=NA_VALUES, keep_default_na=False,
                       low_memory=False)


def main():
    p = argparse.ArgumentParser(description="Compare shared columns across datasets.")
    p.add_argument("csv_paths", nargs="+", help="Two or more CSV files to compare.")
    p.add_argument("--out", default="CROSS_DATASET.md")
    args = p.parse_args()

    frames = {os.path.basename(pth): load(pth) for pth in args.csv_paths}
    names = list(frames)

    # Shared vs unique columns
    col_sets = {n: set(df.columns) for n, df in frames.items()}
    shared = set.intersection(*col_sets.values())
    lines = ["# Cross-Dataset Comparison\n",
             f"Datasets compared: {', '.join(names)}\n",
             "## Column overlap\n",
             f"- **Shared by all {len(names)} datasets ({len(shared)}):** "
             f"{', '.join(sorted(shared)) or '(none)'}\n"]
    for n in names:
        unique = col_sets[n] - shared
        lines.append(f"- **Unique to `{n}` ({len(unique)}):** "
                     f"{', '.join(sorted(unique)) or '(none)'}\n")

    # Shared numeric columns: compare summary stats across datasets
    lines.append("\n## Shared numeric columns — summary by dataset\n")
    shared_numeric = []
    for col in sorted(shared):
        if all(pd.api.types.is_numeric_dtype(frames[n][col]) for n in names):
            shared_numeric.append(col)

    if not shared_numeric:
        lines.append("_No shared columns were numeric in all datasets. "
                     "Comparison would require normalizing types first._\n")
    else:
        for col in shared_numeric:
            lines.append(f"\n### `{col}`\n")
            lines.append("| dataset | count | mean | std | min | median | max |")
            lines.append("|---|---|---|---|---|---|---|")
            for n in names:
                s = frames[n][col]
                lines.append(
                    f"| {n} | {int(s.count()):,} | {s.mean():,.2f} | {s.std():,.2f} "
                    f"| {s.min():,.2f} | {s.median():,.2f} | {s.max():,.2f} |"
                )

    # Shared non-numeric columns: compare cardinality + top value
    lines.append("\n## Shared non-numeric columns — cardinality by dataset\n")
    shared_text = [c for c in sorted(shared) if c not in shared_numeric]
    if shared_text:
        lines.append("| column | " + " | ".join(names) + " |")
        lines.append("|---|" + "|".join(["---"] * len(names)) + "|")
        for col in shared_text:
            cells = []
            for n in names:
                nun = frames[n][col].nunique(dropna=True)
                cells.append(f"{nun:,} unique")
            lines.append(f"| {col} | " + " | ".join(cells) + " |")
    else:
        lines.append("_No shared non-numeric columns._\n")

    report = "\n".join(lines) + "\n"
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(report)
    print(report)
    print(f"[ok] Wrote {args.out}")


if __name__ == "__main__":
    main()
