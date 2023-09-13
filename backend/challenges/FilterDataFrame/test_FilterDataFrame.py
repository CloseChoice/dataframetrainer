# This is sent to the client for testing
#

from challenges.FilterDataFrame.FilterDataFrame import (
    FilterDataFrame,
)
import pandas.testing as tm
from hypothesis import given
import challenges.FilterDataFrame.submission as submission

import importlib
importlib.reload(submission)

@given(**FilterDataFrame.create_df_func())
def test_transform(df):
    expected_df = FilterDataFrame.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)

