"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
from collections.abc import Callable

from hypothesis import assume
import hypothesis.strategies as st

CITIES = ["Las Vegas", "London", "Berlin", "Madrid", "Sao Paulo", "Nairobi", "Sydney", "Moscau", "Kairo", "Tokyo"]
CITY_INHABITANTS = {
    "Las Vegas": 650_000,
    "London": 8_900_000,
    "Berlin": 3_700_000,
    "Madrid": 3_200_000,
    "Sao Paulo": 12_000_000,
    "Nairobi": 4_500_000,
    "Sydney": 5_200_000,
    "Moscau": 12_000_000,
    "Kairo": 20_000_000,
    "Tokyo": 13_900_000
}

@st.composite
def df_trusted(draw, common_indices):
    num_additional_rows = draw(st.integers(min_value=1, max_value=3))
    common_indices = draw(common_indices)
    data = []
    for idx in common_indices:
        city = CITIES[idx]
        if draw(st.booleans()):
            data.append([city, CITY_INHABITANTS[city]])
        else:
            data.append([city, -1])
    for _ in range(num_additional_rows):
        city = draw(st.sampled_from(CITIES))
        data.append([city, CITY_INHABITANTS[city]])
    return pd.DataFrame(data, columns=["city", "inhabitants"])
    
@st.composite
def df_noisy(draw, common_indices):
    additional_indices = []
    num_additional_indices = draw(st.integers(min_value=1, max_value=3))
    common_indices = draw(common_indices)
    for _ in range(num_additional_indices):
        additional_indices.append(draw(st.integers(min_value=0, max_value=len(CITIES) - 1).filter(lambda x: x not in common_indices)))
    data = []
    for idx in common_indices:
        city = CITIES[idx]
        if draw(st.booleans()):
            data.append([city, CITY_INHABITANTS[city]])
        else:
            noise = draw(st.integers(min_value=-10, max_value=10))
            data.append([city, CITY_INHABITANTS[city] + noise * 100_000]) 
    for idx in additional_indices:
        city = CITIES[idx] 
        data.append([city, CITY_INHABITANTS[city]])
    return pd.DataFrame(data, columns=["city", "inhabitants"])

@st.composite
def generate_common_indices(draw):
    return draw(st.lists(st.integers(min_value=0, max_value=len(CITIES) - 1), min_size=1, max_size=3, unique=True))

class FixConflictingDataFrames:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        num_common_indices = generate_common_indices()
        return {"df_trusted": df_trusted(num_common_indices), "df_noisy": df_noisy(num_common_indices)}

    @staticmethod
    def transform(df_trusted: pd.DataFrame, df_noisy: pd.DataFrame) -> pd.DataFrame:
        df = pd.concat([df_trusted, df_noisy]).drop_duplicates(keep="first")
        return df[df["inhabitants"] != -1]

    @staticmethod
    def static_example() -> dict[str, pd.DataFrame]:
        df_trusted = pd.DataFrame(
            [
               ["Las Vegas", 650_000],
               ["Tokyo", 13_900_000],
               ["Berlin", -1],  # Unfortunately, this dataframe has no information for Berlin
            ], columns=["city", "inhabitants"]
        )
        df_noisy = pd.DataFrame(
            [
                ["Berlin", 3_800_000],  # This is noisy. Berlin has 3_700_000 inhabitants
                ["Tokyo", 14_900_000]   # This is noisy. Tokyo has 13_900_000 inhabitants
            ], columns=["city", "inhabitants"]
        )
        return {"df_trusted": df_trusted, "df_noisy": df_noisy}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["Las Vegas", 650_000],
                ["Tokyo", 13_900_000],
                ["Berlin", 3_800_000],
            ],
            columns=["city", "inhabitants"],
        )