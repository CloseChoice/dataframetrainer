"""Map values in a column with the following rules: 1 -> 100, 2 -> 0.5, 3 -> 1"""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, range_indexes
import hypothesis.strategies as st


class MapValues():
    @staticmethod
    def initial() -> pd.DataFrame:
        # todo: this somehow generates floats in the number_col column, this should be changed
        return data_frames(
            columns=[
                column("number_col", dtype=np.dtype(int)),
            ],
            rows=st.tuples(st.sampled_from([1, 2, 3])),
            index=range_indexes(min_size=3, max_size=10),
        ).example()

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df["number_col"] = df.number_col.map({1: 100, 2: 0.5, 3: 1})
        return df

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1],
                [2],
                [3],
                [2],
                [3],
            ],
            columns=["number_col"],
        )

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [100],
                [0.5],
                [1],
                [0.5],
                [1],
            ],
            columns=["number_col"],
        )
