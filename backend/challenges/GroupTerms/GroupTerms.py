"""Group and count the appearances of the single terms"""
"""inspired by: https://stackoverflow.com/questions/39132742/groupby-value-counts-on-the-dataframe-pandas"""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, range_indexes
import hypothesis.strategies as st


class GroupTerms:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        # todo: this somehow generates floats in the number column, this should be changed
        return {"df": data_frames(
            columns=[
                column("id", dtype=np.dtype(str)),
                column("group", dtype=np.dtype(str)),
                column("term", dtype=np.dtype(str)),
            ],
            rows=st.tuples(
                st.integers(
                    min_value=1,
                    max_value=2,
                ),
                st.integers(
                    min_value=1,
                    max_value=3,
                ),
                st.sampled_from(["term1", "term2", "term3"]),
            ),
            index=range_indexes(min_size=3, max_size=10),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        return df.groupby(["id", "group", "term"]).size().unstack(fill_value=0)

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        return_df = pd.DataFrame(
            [
                (1, 1, "term1"),
                (1, 2, "term2"),
                (1, 1, "term1"),
                (1, 1, "term2"),
                (2, 2, "term3"),
                (2, 3, "term1"),
                (2, 2, "term1"),
            ],
            columns=["id", "group", "term"],
        )
        return {"df": return_df}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [[2, 1, 0], [0, 1, 0], [1, 0, 1], [1, 0, 0]],
            columns=pd.Index(["term1", "term2", "term3"], name="term"),
            index=pd.MultiIndex.from_tuples(
                [(1, 1), (1, 2), (2, 2), (2, 3)], names=["id", "group"]
            ),
        )
