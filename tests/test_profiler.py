"""
Contract tests. These FAIL against the starter stubs — make them pass, then
keep them green as you build out the report.
"""
import pandas as pd
from profiler import load_csv, profile


def _sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "price": [10.0, 12.0, 11.0, 9.0, 5000.0, None],  # 5000 is an outlier
            "qty":   [1, 2, 1, 3, 2, 2],
            "country": ["AU", "US", "AU", None, "US", "AU"],
        }
    )


def test_load_returns_dataframe(tmp_path):
    p = tmp_path / "t.csv"
    p.write_text("a,b\n1,2\n3,4\n")
    df = load_csv(str(p))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2


def test_profile_detects_missing_and_duplicates():
    prof = profile(_sample_df())
    assert prof["n_rows"] == 6
    # price and country each have one missing value
    assert prof["missing"]["price"]["count"] == 1
    assert prof["missing"]["country"]["count"] == 1


def test_outlier_detection_flags_extreme_value():
    prof = profile(_sample_df())
    # The 5000 price must be flagged by the IQR rule
    assert prof["outliers"]["price"] >= 1
