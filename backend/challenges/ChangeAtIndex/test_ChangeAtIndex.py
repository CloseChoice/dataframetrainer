# This is sent to the client for testing
#

from challenges.ChangeAtIndex.ChangeAtIndex import (
    ChangeAtIndex,
)
import pandas.testing as tm
from hypothesis import given
import challenges.ChangeAtIndex.submission as submission

import importlib
importlib.reload(submission)

@given(**ChangeAtIndex.create_df_func())
def test_transform(df):
    expected_df = ChangeAtIndex.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
