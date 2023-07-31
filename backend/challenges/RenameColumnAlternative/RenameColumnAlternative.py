import hypothesis.strategies as st
from hypothesis.extra.pandas import data_frames, column, range_indexes
import numpy as np
import pandas as pd
import pandas.testing as tm


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={"Value": "NewValue"})
    return df

# Since the "run" "initial" and "test" use cases all rely on the same param generators it makes sense to share them
# Possibly as a dict 
params = {
    'df': data_frames(
        columns=[column("Value", dtype=np.dtype(int))],
        rows=st.tuples(st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),),
        index=range_indexes(min_size=3, max_size=10),
    )
}

# The "run" and "initial" methods are always the same regardless of challenge
# Therefore they could be implemented in a "Challenge" Class
# To ensure same imports in local development and pyodide the "Challenge" Class would have to be a module
# challenge = Challenge(params, transform)


"""Rename the column `Value` to `NewValue`"""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes
import hypothesis.strategies as st
from hypothesis import given, settings
from collections.abc import Callable


class RenameColumnAlternative:
    @staticmethod
    def create_df_func() -> Callable:
        return data_frames(
            columns=[
                column("Value", dtype=np.dtype(int)),
            ],
            rows=st.tuples(
                st.sampled_from([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ),
            index=range_indexes(min_size=3, max_size=10),
        )

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df = df.rename(columns={"Value": "NewValue"})
        return df

    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame([[1], [2], [3]], columns=["Value"])

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame([[1], [2], [3]], columns=["NewValue"])