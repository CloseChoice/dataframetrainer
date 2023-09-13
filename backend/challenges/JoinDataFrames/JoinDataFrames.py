"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.numpy import arrays
from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st
import uuid

LIST_OF_NAMES = ["James", "Mary",
                 "Robert", "Patricia",
                 "John", "Jennifer",
                 "Michael", "Linda",
                 "David", "Elizabeth",
                 "William", "Barbara",
                 "Richard", "Susan",
                 "Joseph", "Jessica",
                 "Thomas", "Sarah",
                 "Christopher", "Karen",
                 "Charles", "Lisa",
                 "Daniel", "Nancy",
                 "Matthew", "Betty",
                 "Anthony", "Sandra",
                 "Mark", "Margaret",
                 "Donald", "Ashley",
                 "Steven", "Kimberly",
                 "Andrew", "Emily",
                 "Paul", "Donna",
                 "Joshua", "Michelle"]

@st.composite
def generate_df1(draw):
    uuids = draw(st.shared(st.lists(st.uuids(), min_size=2, max_size=2), key="common_uuids"))
    integer_list = draw(st.lists(st.integers(min_value=0, max_value=1000), min_size=2, max_size=2))
    df1 = pd.DataFrame({"customerId": uuids, "customerSpendings": integer_list})
    return df1

@st.composite
def generate_df2(draw):
    uuids = draw(st.shared(st.lists(st.uuids(), min_size=2, max_size=2), key="common_uuids"))
    names = draw(st.lists(st.sampled_from(LIST_OF_NAMES), min_size=2, max_size=2))
    df2 = pd.DataFrame({"customerId": uuids, "customerName": names})
    return df2

class JoinDataFrames:

    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df1": generate_df1(), "df2": generate_df2()}

    @staticmethod
    def transform(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        return pd.merge(df1, df2, on="customerId")

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        uuids = [uuid.UUID('057bdfb8-78fd-4101-8f24-17ac4bba68f8'),
                 uuid.UUID('35c8b4fe-deec-4acc-ad25-3850f29137ab')]
        df1 = pd.DataFrame(
            [
                [uuids[0], 100],
                [uuids[1], 200]
            ], columns=["customerId", "customerSpendings"]
        )
        df2 = pd.DataFrame(
            [
                [uuids[0], "Charles"],
                [uuids[1], "Andrew"]
            ], columns=["customerId", "customerSpendings"]
        )
        return {"df1": df1, "df2": df2}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [uuid.UUID('057bdfb8-78fd-4101-8f24-17ac4bba68f8'), 100, "Charles"],
                [uuid.UUID('35c8b4fe-deec-4acc-ad25-3850f29137ab'), 200, "Andrew"]
            ],
            columns=["customerId", "customerSpendings", "customerName"],
        )