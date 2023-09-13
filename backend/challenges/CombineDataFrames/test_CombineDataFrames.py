# This is sent to the client for testing
#

from challenges.CombineDataFrames.CombineDataFrames import (
    CombineDataFrames,
)
import pandas.testing as tm
from hypothesis import given
import challenges.CombineDataFrames.submission as submission

import importlib
importlib.reload(submission)

@given(**CombineDataFrames.create_df_func())
def test_transform(series1, series2):
    expected_df = CombineDataFrames.transform(series1, series2)
    user_df = submission.transform(series1, series2)
    tm.assert_frame_equal(user_df, expected_df)

