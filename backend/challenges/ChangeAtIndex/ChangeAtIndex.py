"""Change the the Value of the third element (index 2) to -100"""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st


class ChangeAtIndex:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df": data_frames(
            columns=[
                column("Value", dtype=np.dtype(int)),
                column("Name", dtype=np.dtype(str)),
            ],
            rows=st.tuples(
                st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                st.sampled_from(["Helmut", "Greta", "Siegfried"]),
            ),
            index=range_indexes(min_size=3, max_size=5),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df.loc[2, "Value"] = -100
        return df

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        return_df = pd.DataFrame(
            [[1, "Helmut"], [2, "Greta"], [3, "Siegfried"]], columns=["Value", "Other"]
        )
        return {"df": return_df}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [[1, "Helmut"], [2, "Greta"], [-100, "Siegfried"]],
            columns=["Value", "Other"],
        )
