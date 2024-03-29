"""Sum the spendings per Customer."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.pandas import data_frames, column, indexes
import hypothesis.strategies as st


class SumSpendings:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df": data_frames(
            columns=[
                column("Customer", dtype=np.dtype(str)),
                column("Spendings", dtype=np.dtype(float)),
            ],
            rows=st.tuples(
                st.sampled_from(["Helmut", "Greta", "Siegfried"]),
                st.floats(
                    allow_infinity=False,
                    allow_nan=False,
                    allow_subnormal=False,
                    min_value=0.0,
                    max_value=1000,
                    width=16,
                    exclude_min=True,
                ),
            ),
            index=indexes(
                min_size=1, elements=st.integers(min_value=1, max_value=20), dtype=int
            ),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.Series:
        return df.groupby("Customer")[["Spendings"]].sum()
    
    @staticmethod
    def static_example() -> pd.DataFrame:
        return {"df": pd.DataFrame(
            [
                ["Helmut", 100],
                ["Greta", 200],
                ["Siegfried", 300],
                ["Helmut", 400],
                ["Greta", 500],
                ["Siegfried", 600],
            ],
            columns=["Customer", "Spendings"],
        )}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [500],
                [700],
                [900],
            ],
            columns=["Spendings"],
            index=pd.Index(['Greta', 'Helmut', 'Siegfried'], name='Customer')
        )