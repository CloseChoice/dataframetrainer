# This is sent to the client for testing
#

from challenges.FixConflictingDataFrames.FixConflictingDataFrames import (
    FixConflictingDataFrames,
)
import pandas.testing as tm
import pandas as pd
from hypothesis import given
import challenges.FixConflictingDataFrames.submission as submission

import importlib
importlib.reload(submission)

@given(**FixConflictingDataFrames.create_df_func())
def test_transform(df_trusted: pd.DataFrame, df_noisy: pd.DataFrame):
    expected_df = FixConflictingDataFrames.transform(df_trusted, df_noisy)
    user_df = submission.transform(df_trusted, df_noisy)
    tm.assert_frame_equal(user_df.sort_values(list(user_df.columns)).reset_index(drop=True),
                          expected_df.sort_values(list(user_df.columns)).reset_index(drop=True))

