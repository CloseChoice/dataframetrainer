"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
import hypothesis
from collections.abc import Callable

from hypothesis.extra.numpy import arrays


class CreateDataFrameFromArray:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        array = arrays(np.int8, (4, 2))
        return {"array": array}

    @staticmethod
    def transform(array: np.ndarray) -> pd.DataFrame:
        return pd.DataFrame(array, columns=["col_1", "col_2"])

    @staticmethod
    def static_example() -> np.ndarray:
        return np.array([[1, 2], [3, 4]])

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                [1, 2],
                [3, 4]
            ],
            index=["col_1", "col_2"], columns=["col_1", "col_2"],
        )