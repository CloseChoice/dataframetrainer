"""Rename the column `Value` to `NewValue`"""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st
from hypothesis import given, settings
from collections.abc import Callable


class RenameColumn:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {
            "df": data_frames(
                columns=[
                    column("Value", dtype=np.dtype(int)),
                ],
                rows=st.tuples(
                    st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                ),
                index=range_indexes(min_size=3, max_size=10),
            )
        }

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df = df.rename(columns={"Value": "NewValue"})
        return df

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        return {"df": pd.DataFrame([[1], [2], [3]], columns=["Value"])}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame([[1], [2], [3]], columns=["NewValue"])
