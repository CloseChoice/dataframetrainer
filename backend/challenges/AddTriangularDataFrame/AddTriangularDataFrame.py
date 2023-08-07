"""Add a triangular DataFrame to a given pandas Series"""
"""inspired by: https://stackoverflow.com/questions/73536536/how-to-generate-a-triangular-data-frame-with-as-many-columns-as-the-row-indica"""
import pandas as pd
import numpy as np
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st


class AddTriangularDataFrame:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df": data_frames(
            columns=[
                column("number", dtype=np.dtype(int)),
            ],
            rows=st.tuples(
                st.integers(
                    min_value=1,
                    max_value=100,
                )
            ),
            index=range_indexes(min_size=3, max_size=10),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.Series:
        df_intermediate = pd.DataFrame(
            np.tril(np.ones((len(df), len(df))) * np.arange(len(df)) + 1),
            columns=[f"C{i}" for i in range(1, len(df) + 1)],
        )
        return pd.concat([df, df_intermediate], axis=1).astype(int)

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1],
                [2],
                [3],
                [4],
                [5],
                [6],
            ],
            columns=["number"],
        )

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, 1, 0, 0, 0, 0, 0],
                [2, 1, 2, 0, 0, 0, 0],
                [3, 1, 2, 3, 0, 0, 0],
                [4, 1, 2, 3, 4, 0, 0],
                [5, 1, 2, 3, 4, 5, 0],
                [6, 1, 2, 3, 4, 5, 6],
            ],
            columns=["number", "C1", "C2", "C3", "C4", "C5", "C6"],
        )
