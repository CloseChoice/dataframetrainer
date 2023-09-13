# This is sent to the client for testing
#

from challenges.AntiJoinDataFrames.AntiJoinDataFrames import (
    AntiJoinDataFrames,
)
import pandas.testing as tm
import pandas as pd
from hypothesis import given
import challenges.AntiJoinDataFrames.submission as submission

import importlib
importlib.reload(submission)

@given(**AntiJoinDataFrames.create_df_func())
def test_transform(df_today: pd.DataFrame, df_yesterday: pd.DataFrame):
    expected_df = AntiJoinDataFrames.transform(df_today, df_yesterday)
    user_df = submission.transform(df_today, df_yesterday)
    tm.assert_frame_equal(user_df, expected_df)

