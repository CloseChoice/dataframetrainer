"""Inspired by: https://stackoverflow.com/a/19913845/9534390. Implement the following conditions:
If Set is Z and Type is A then Color is green, if Set is Z and Type is B then color red, if if Set is not Z and Type is B then color pink, otherwise black"""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
import hypothesis.strategies as st


class TransformWithMultipleConditions:
    @staticmethod
    def initial() -> pd.DataFrame:
        # todo: this is not optimal, but it works for now
        # things to improve:
        #   - use one of the strategies from hypothesis.extra.pandas to generate the whole df, don't use pd.concat
        #   - length of the df should be variable
        #   - np.nan should be generated in the value column, but this is not possible if one specifies min and max values
        return data_frames(
            columns=[
                column("Type", dtype=np.dtype(str)),
                column("Set", dtype=np.dtype(str)),
            ],
            rows=st.tuples(
                st.sampled_from(["A", "B", "C"]), st.sampled_from(["X", "Y", "Z"])
            ),
            index=range_indexes(min_size=3, max_size=8),
        ).example()

    @staticmethod
    def transform(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        conditions = [
            (df["Set"] == "Z") & (df["Type"] == "A"),
            (df["Set"] == "Z") & (df["Type"] == "B"),
            (df["Type"] == "B"),
        ]
        choices = ["green", "red", "pink"]
        df["Color"] = np.select(conditions, choices, default="black")
        return df

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["A", "Z"],
                ["B", "Z"],
                ["B", "X"],
                ["C", "Y"],
            ],
            columns=["Type", "Set"],
        )

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["A", "Z", "green"],
                ["B", "Z", "red"],
                ["B", "X", "pink"],
                ["C", "Y", "black"],
            ],
            columns=["Type", "Set", "Color"],
        )
