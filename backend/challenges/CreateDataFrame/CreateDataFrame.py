"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

import hypothesis.strategies as st


class CreateDataFrame:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        size = 7
        list1 = st.lists(st.integers(min_value=0, max_value=10), min_size=size, max_size=size)
        list2 = st.lists(st.floats(min_value=0, max_value=5), min_size=size, max_size=size)
        list3 = st.lists(st.characters(), min_size=size, max_size=size)
        return {"list1": list1, "list2": list2, "list3": list3}

    @staticmethod
    def transform(list1: list[int], list2: list[float], list3: list[str]) -> pd.DataFrame:
        return pd.DataFrame({"integer_list": list1, "float_list": list2, "string_list": list3},
                            columns=["string_list", "float_list", "integer_list"])

    @staticmethod
    def static_example() -> dict[str, list[int | float | str]]:
        list1 = [1, 2, 3, 4, 5]
        list2 = [-1.0, 2.0, 3.0, 4.0, 5.0]
        list3 = ["a", "b", "c", "d", "e"]
        
        return {"list1": list1, "list2": list2, "list3": list3}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["a", 1., 1],
                ["b", 2., 2],
                ["c", 3., 3],
                ["d", 4., 4],
                ["e", 5., 5],
            ],
            columns=["string_list", "float_list", "integer_list"],
        )