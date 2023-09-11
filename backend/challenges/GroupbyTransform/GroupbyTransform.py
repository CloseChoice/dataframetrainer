"""Inspired by: https://stackoverflow.com/questions/37189878/pandas-add-column-to-groupby-dataframe.
 The goal is to count values of type for each `value`, and then add a column with the size of `value."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
import hypothesis.strategies as st


class GroupbyTransform:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        # todo: this is not optimal, but it works for now
        # things to improve:
        #   - use one of the strategies from hypothesis.extra.pandas to generate the whole df, don't use pd.concat
        #   - length of the df should be variable
        #   - np.nan should be generated in the value column, but this is not possible if one specifies min and max values
        return {"df": data_frames(
            columns=[
                column("value", dtype=np.dtype(str)),
                column("group", dtype=np.dtype(str)),
            ],
            rows=st.tuples(st.sampled_from([1, 2]), st.sampled_from(["m", "n", "o"])),
            index=range_indexes(min_size=3, max_size=8),
        )}

    @staticmethod
    def transform(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df["size"] = df.groupby("value")["group"].transform(len)
        # alternative
        # df['size'] = df['c'].map(df['c'].value_counts())
        return df

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        return_df = pd.DataFrame(
            {
                "value": [1, 1, 1, 2, 2, 2, 2],
                "group": ["m", "n", "o", "m", "m", "n", "n"],
            }
        )
        return {"df": return_df}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, "m", 3],
                [1, "n", 3],
                [1, "o", 3],
                [2, "m", 4],
                [2, "m", 4],
                [2, "n", 4],
                [2, "n", 4],
            ],
            columns=["value", "group", "size"],
        )
