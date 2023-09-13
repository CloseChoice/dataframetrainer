"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from copy import copy
from hypothesis.extra.numpy import arrays
from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
from hypothesis import assume
import hypothesis.strategies as st
import uuid

@st.composite
def df_today(draw):
    uuid1, uuid2 = draw(st.shared(st.lists(st.uuids(), min_size=2, max_size=2), key="common_uuids"))
    integer_list = draw(st.lists(st.integers(min_value=0, max_value=1000), min_size=2, max_size=2))
    return pd.DataFrame({"customerId": [uuid1, uuid2], "customerSpendings": integer_list})
    
@st.composite
def df_yesterday(draw):
    uuid1, uuid2 = draw(st.shared(st.lists(st.uuids(), min_size=2, max_size=2), key="common_uuids"))
    integer_list = draw(st.lists(st.integers(min_value=0, max_value=1000), min_size=3, max_size=3))
    uuid3 = draw(st.uuids().filter(lambda x: x not in [uuid1, uuid2]))
    return pd.DataFrame({"customerId": [uuid1, uuid2, uuid3], "customerSpendings": integer_list})


class AntiJoinDataFrames:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df_today": df_today(), "df_yesterday": df_yesterday()}

    @staticmethod
    def transform(df_today: pd.DataFrame, df_yesterday: pd.DataFrame) -> pd.DataFrame:
        return df_yesterday[~df_yesterday["customerId"].isin(df_today["customerId"])]

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        uuids = [uuid.UUID('057bdfb8-78fd-4101-8f24-17ac4bba68f8'),
                 uuid.UUID('35c8b4fe-deec-4acc-ad25-3850f29137ab'),
                 uuid.UUID('0e99d745-26aa-4ba3-8f92-34b54a1a47fa')
                 ]
        df_today = pd.DataFrame(
            [
                [uuids[0], 100],
                [uuids[1], 200]
            ], columns=["customerId", "customerSpendings"]
        )
        df_yesterday = pd.DataFrame(
            [
                [uuids[0], 1000],
                [uuids[1], 2000],
                [uuids[2], 3000]
            ]
        )
        return {"df_today": df_today, "df_yesterday": df_yesterday}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [uuid.UUID('0e99d745-26aa-4ba3-8f92-34b54a1a47fa'), 3000]
            ],
            columns=["customerId", "customerSpendings"],
        )