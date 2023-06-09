"""Get the highest expense for each customer-type combination. The types shall be columns, while the customer should be the index.
Treat missing values as np.nan. If a Customer does not appear in the initial dataframe, don't add a row for this customer."""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
import hypothesis.strategies as st

from .BaseChallenge import BaseChallenge


class Pivot1(BaseChallenge):
    @staticmethod
    def initial() -> pd.DataFrame:
        return data_frames(
            columns=[
                column("Customer", dtype=np.dtype(str)),
                column("Type", dtype=np.dtype(str)),
                column("Expense", dtype=np.dtype(int)),
            ],
            rows=st.tuples(
                st.sampled_from(["Harald", "Helga", "Friedrich"]),
                st.sampled_from(["Groceries", "Electronics", "Entertainment"]),
                st.integers(min_value=-1, max_value=1000),
            ),
            index=range_indexes(min_size=3, max_size=12),
        ).example()

    @staticmethod
    def transform(df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        df = df.pivot_table(
            index="Customer", columns="Type", values="Expense", aggfunc=np.max
        )
        return df

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["Harald", "Groceries", 1],
                ["Harald", "Groceries", 100],
                ["Harald", "Groceries", 1000],
                ["Harald", "Electronics", 20],
                ["Harald", "Entertainment", 20],
                ["Helga", "Entertainment", 20],
                ["Helga", "Groceries", 4],
                ["Friedrich", "Groceries", -1],
                ["Friedrich", "Groceries", 10],
            ],
            columns=["Customer", "Type", "Expense"],
        )

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [np.nan, np.nan, 10.0],
                [20.0, 20.0, 1000.0],
                [np.nan, 20.0, 4.0],
            ],
            columns=["Electronics", "Entertainment", "Groceries"],
            index=["Friedrich", "Harald", "Helga"],
        )
