# This is sent to the client for testing
#

from challenges.JoinDataFrames.JoinDataFrames import (
    JoinDataFrames,
)
import pandas.testing as tm
from hypothesis import given
import challenges.JoinDataFrames.submission as submission

import importlib
importlib.reload(submission)

@given(**JoinDataFrames.create_df_func())
def test_transform(df1, df2):
    expected_df = JoinDataFrames.transform(df1, df2)
    user_df = submission.transform(df1, df2)
    tm.assert_frame_equal(user_df, expected_df)

