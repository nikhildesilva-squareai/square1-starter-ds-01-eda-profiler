"""
Core profiler. Implement the three functions below — the tests in
tests/test_profiler.py define the contract each must satisfy.

Tip: lean on pandas. Keep functions small and pure where you can.
"""
from __future__ import annotations
import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV into a DataFrame.

    TODO: read the CSV at `path` and return a DataFrame.
    Decide how to treat blank strings (hint: they should count as missing).
    """
    raise NotImplementedError("Implement load_csv")


def profile(df: pd.DataFrame) -> dict:
    """Return a profile dict describing `df`.

    TODO: return at least:
      - "n_rows", "n_cols"
      - "dtypes": {column: inferred_type}
      - "missing": {column: {"count": int, "pct": float}}
      - "duplicate_rows": int                      # exact duplicate rows
      - "numeric_summary": {column: {min,max,mean,median,std}}
      - "outliers": {column: int}                  # count via the IQR rule
      - "categorical_top": {column: [(value, count), ...]}
      - "correlations": {colA: {colB: r}}          # numeric columns only
    """
    raise NotImplementedError("Implement profile")


def to_html(profile_data: dict, out_path: str) -> None:
    """Render `profile_data` to a self-contained HTML report at `out_path`.

    TODO: build an HTML report (jinja2 recommended) with the five sections
    from the brief, including at least one distribution plot and a
    correlation heatmap (matplotlib/seaborn → embed as base64 <img>).
    """
    raise NotImplementedError("Implement to_html")
