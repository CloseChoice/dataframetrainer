"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import series, column, range_indexes
import hypothesis.strategies as st


class CombineDataFrames:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        index = range_indexes(min_size=4, max_size=7)
        series1 = series(elements=st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]), index=index)
        series2 = series(elements=st.sampled_from(list("abcdefghijklmnopqrstuvwxyz")), index=index)
        return {"series1": series1, "series2": series2}

    @staticmethod
    def transform(series1: pd.Series, series2: pd.Series) -> pd.DataFrame:
        return pd.DataFrame({"series1": series1, "series2": series2})

    @staticmethod
    def static_example() -> dict[str, pd.Series]:
        index = range(0, 5)
        series1 = pd.Series([1, 2, 3, 4, 5], index=index)
        series2 = pd.Series(["a", "b", "c", "d", "e"], index=index)
        return {"series1": series1, "series2": series2}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [0, "a"],
                [1, "b"],
                [2, "c"],
                [3, "d"],
                [4, "e"],
            ],
            columns=["series1", "series2"],
        )