"""Command-line entry point:  python -m profiler.cli data.csv --out report.html"""
import argparse
from .profiler import load_csv, profile, to_html


def main() -> None:
    ap = argparse.ArgumentParser(description="Profile a CSV and write an HTML report.")
    ap.add_argument("csv", help="Path to the CSV file to profile")
    ap.add_argument("--out", default="report.html", help="Output HTML path")
    args = ap.parse_args()

    df = load_csv(args.csv)
    prof = profile(df)
    to_html(prof, args.out)
    print(f"Wrote {args.out} ({prof.get('n_rows', '?')} rows profiled)")


if __name__ == "__main__":
    main()
