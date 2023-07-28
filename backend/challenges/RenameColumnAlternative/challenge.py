import hypothesis.strategies as st
from hypothesis.extra.pandas import data_frames, column, range_indexes
import numpy as np
import pandas as pd
import pandas.testing as tm

import Challenge from ??


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
challenge = Challenge(params, transform)