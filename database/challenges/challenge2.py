"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, indexes
import hypothesis.strategies as st

from .BaseChallenge import BaseChallenge


class ChangeDependingOfOthers(BaseChallenge):
    @staticmethod
    def initial() -> pd.DataFrame:
        return data_frames(
            columns=[
                column("Value", dtype=np.dtype(float)),
                column("Other", dtype=np.dtype(str)),
            ],
            rows=st.tuples(
                st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                st.sampled_from(["Helmut", "Greta", "Siegfried"]),
            ),
            index=indexes(
                min_size=5, elements=st.integers(min_value=1, max_value=20), dtype=int
            ),
        ).example()

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df["Value"] = np.where(df["Value"] <= 3, df["Value"], 100)
        return df
