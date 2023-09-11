"""Add a new column `Date` where the date increases by one month from row to row, starting from 2023-01-01.
(So 2023-02-01, 2023-03-01, etc. depending of the length of the dataframe)"""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st

from pandas.tseries.offsets import DateOffset


class MonthIndex:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df": data_frames(
            columns=[
                column("Value", dtype=np.dtype(int)),
            ],
            rows=st.tuples(
                st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ),
            index=range_indexes(min_size=3, max_size=10),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df.loc[:, "Date"] = pd.date_range(
            "2023-01-01", freq=DateOffset(months=1), periods=len(df)
        )
        return df

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        return_df = pd.DataFrame([[1], [2], [3]], columns=["Value"])
        return {"df": return_df}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, pd.to_datetime("2023-01-01")],
                [2, pd.to_datetime("2023-02-01")],
                [3, pd.to_datetime("2023-03-01")],
            ],
            columns=["Value", "Date"],
        )
