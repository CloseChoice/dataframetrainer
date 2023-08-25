"""Add a pseudo-triangular DataFrame to a given pandas Series"""
"""inspired by: https://stackoverflow.com/questions/73536536/how-to-generate-a-triangular-data-frame-with-as-many-columns-as-the-row-indica"""
import pandas as pd
import numpy as np
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st


class Challenge:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        # todo: this somehow generates floats in the number column, this should be changed
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
            index=indexes(
                min_size=5,
                max_size=10,
                elements=st.integers(min_value=1, max_value=10),
                dtype=int,
            ),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        return df.join(
            pd.DataFrame(
                df["number"]
                # todo: remove casting to int once the issue with the floats above is fixed
                .map(lambda x: range(1, int(x) + 1)).tolist()
            ).rename(lambda x: "C{}".format(x + 1), axis=1)
        )

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1],
                [2],
                [3],
                [4],
                [6],
            ],
            columns=["number"],
        )

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, 1, np.nan, np.nan, np.nan, np.nan, np.nan],
                [2, 1, 2, np.nan, np.nan, np.nan, np.nan],
                [3, 1, 2, 3, np.nan, np.nan, np.nan],
                [4, 1, 2, 3, 4, np.nan, np.nan],
                [6, 1, 2, 3, 4, 5, 6],
            ],
            columns=["number", "C1", "C2", "C3", "C4", "C5", "C6"],
        )
