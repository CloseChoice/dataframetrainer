"""Rename the column `Value` to `NewValue`"""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st

from .BaseChallenge import BaseChallenge


class RenameColumn(BaseChallenge):
    @staticmethod
    def initial() -> pd.DataFrame:
        return data_frames(
            columns=[
                column("Value", dtype=np.dtype(int)),
            ],
            rows=st.tuples(
                st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ),
            index=range_indexes(min_size=3, max_size=10),
        ).example()

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df = df.rename(columns={"Value": "NewValue"})
        return df

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame([[1], [2], [3]], columns=["Value"])

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame([[1], [2], [3]], columns=["NewValue"])
