"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
from collections.abc import Callable

from hypothesis import assume
import hypothesis.strategies as st
import uuid

@st.composite
def unique_uuids_strategy(draw):
    uuid1 = uuid.uuid4()
    uuid2 = uuid.uuid4()
    assume(uuid1 != uuid2)
    return (uuid1, uuid2)

@st.composite
def df_today(draw):
    uuid1, uuid2 = draw(st.shared(st.lists(st.uuids(), min_size=2, max_size=2), key="common_uuids"))
    uuids = [uuid1, uuid2]
    additional_rows = draw(st.integers(min_value=1, max_value=3))
    integer_list = draw(st.lists(st.integers(min_value=0, max_value=1000), min_size=2 + additional_rows, max_size=2 + additional_rows))
    while len(uuids) < len(integer_list):
        uuids.append(draw(st.uuids().filter(lambda x: x not in uuids)))
    np.random.shuffle(uuids)
    return pd.DataFrame({"customerId": uuids, "customerSpendings": integer_list})
    
@st.composite
def df_yesterday(draw):
    uuid1, uuid2 = draw(st.shared(st.lists(st.uuids(), min_size=2, max_size=2), key="common_uuids"))
    integer_list = draw(st.lists(st.integers(min_value=18, max_value=90), min_size=3, max_size=3))
    uuid3 = draw(st.uuids().filter(lambda x: x not in [uuid1, uuid2]))
    uuids = [uuid1, uuid2, uuid3]
    np.random.shuffle(uuids)
    return pd.DataFrame({"customerId": [uuid1, uuid2, uuid3], "customerSpendings": integer_list})


class AntiJoinDataFrames2:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df_customer_today": df_today(), "df_customer_yesterday": df_yesterday()}

    @staticmethod
    def transform(df_customer_today: pd.DataFrame, df_customer_yesterday: pd.DataFrame) -> pd.DataFrame:
        df_merged = pd.merge(df_customer_today, df_customer_yesterday, how="outer", on="customerId", suffixes=("_today", "_yesterday"))
        df_nulls = df_merged[df_merged["customerSpendings_today"].isnull() | df_merged["customerSpendings_today"].isnull()]
        df_nulls["customerSpendings"] = np.where(df_nulls["customerSpendings_today"].isnull(), df_nulls["customerSpendings_yesterday"], df_nulls["customerSpendings_today"])
        df_nulls["day"] = np.where(df_nulls["customerSpendings_today"].isnull(), "yesterday", "today")
        return df_nulls[["customerId", "customerSpendings", "day"]].reset_index(drop=True)

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        uuids = [uuid.UUID('057bdfb8-78fd-4101-8f24-17ac4bba68f8'),
                 uuid.UUID('35c8b4fe-deec-4acc-ad25-3850f29137ab'),
                 uuid.UUID('0e99d745-26aa-4ba3-8f92-34b54a1a47fa'),
                 uuid.UUID('64932494-e446-4d7e-85f7-9039083a03a2')
                 ]
        df_customer_today = pd.DataFrame(
            [
                [uuids[0], 100],
                [uuids[1], 200],
                [uuids[3], 400]
            ], columns=["customerId", "customerSpendings"]
        )
        df_customer_yesterday = pd.DataFrame(
            [
                [uuids[0], 1000],
                [uuids[1], 2000],
                [uuids[2], 3000]
            ], columns=["customerId", "customerSpendings"]
        )
        return {"df_customer_today": df_customer_today, "df_customer_yesterday": df_customer_yesterday}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [uuid.UUID('64932494-e446-4d7e-85f7-9039083a03a2'), 400, "today"],
                [uuid.UUID('0e99d745-26aa-4ba3-8f92-34b54a1a47fa'), 3000, "yesterday"]
            ],
            columns=["customerId", "customerSpendings", "day"],
        )