"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

import hypothesis.strategies as st

LIST_OF_NAMES = ["James", "Mary"
                 "Robert", "Patricia"
                 "John", "Jennifer"
                 "Michael", "Linda"
                 "David", "Elizabeth"
                 "William", "Barbara"
                 "Richard", "Susan"
                 "Joseph", "Jessica"
                 "Thomas", "Sarah"
                 "Christopher", "Karen"
                 "Charles", "Lisa"
                 "Daniel", "Nancy"
                 "Matthew", "Betty"
                 "Anthony", "Sandra"
                 "Mark", "Margaret"
                 "Donald", "Ashley"
                 "Steven", "Kimberly"
                 "Andrew", "Emily"
                 "Paul", "Donna"
                 "Joshua", "Michelle"]

class CreateDataFrameFromDict:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        size = 3
        dict1 = st.dictionaries(keys=st.integers(min_value=0, max_value=10),
                                values=st.lists(st.sampled_from(LIST_OF_NAMES),
                                min_size=size, max_size=size))
        return {"data": dict1}

    @staticmethod
    def transform(data: dict[int, list[str]]) -> pd.DataFrame:
        return pd.DataFrame.from_dict(data)

    @staticmethod
    def static_example() -> dict[str, list[int | float | str]]:
        return {'col_1': ["Charles", "Lisa"], 'col_2': ["Andrew", "Emily"]}

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["Charles", "Lisa"],
                ["Andrew", "Emily"]
            ],
            columns=["col_1", "col_2"],
        )