"""Inspired by: https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column"""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
import hypothesis.strategies as st


class TransformWithConditions2:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        # todo: this is not optimal, but it works for now
        # things to improve:
        #   - use one of the strategies from hypothesis.extra.pandas to generate the whole df, don't use pd.concat
        #   - length of the df should be variable
        #   - np.nan should be generated in the value column, but this is not possible if one specifies min and max values
        return {"df": data_frames(
            columns=[
                column("Type", dtype=np.dtype(str)),
                column("Set", dtype=np.dtype(str)),
            ],
            rows=st.tuples(
                st.sampled_from(["A", "B", "C"]), st.sampled_from(["X", "Y", "Z"])
            ),
            index=range_indexes(min_size=3, max_size=8),
        )}

    @staticmethod
    def transform(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df["Color"] = np.where(df["Set"] == "Z", "green", "red")
        return df

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        return_df = pd.DataFrame(
            [
                ["A", "Z"],
                ["B", "Z"],
                ["B", "X"],
                ["C", "Y"],
            ],
            columns=["Type", "Set"],
        )
        return {"df": return_df}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["A", "Z", "green"],
                ["B", "Z", "green"],
                ["B", "X", "red"],
                ["C", "Y", "red"],
            ],
            columns=["Type", "Set", "Color"],
        )
