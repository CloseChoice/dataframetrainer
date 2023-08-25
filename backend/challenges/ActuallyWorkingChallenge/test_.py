# This is sent to the client for testing
#

from challenges.ActuallyWorkingChallenge.ActuallyWorkingChallenge import Challenge
import pandas.testing as tm
from hypothesis import given
import challenges.ActuallyWorkingChallenge.submission as submission

import importlib
importlib.reload(submission)

@given(**Challenge.create_df_func())
def test_transform(df):
    expected_df = Challenge.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
