# This is sent to the client for testing
#

from challenges.MonthIndex.MonthIndex import (
    MonthIndex,
)
import pandas.testing as tm
from hypothesis import given
import challenges.MonthIndex.submission as submission

import importlib
importlib.reload(submission)


@given(**MonthIndex.create_df_func())
def test_transform(df):
    expected_df = MonthIndex.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
