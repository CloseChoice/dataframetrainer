# This is sent to the client for testing
#

from challenges.ChangeDependingOnOthers.ChangeDependingOnOthers import (
    ChangeDependingOnOthers,
)
import pandas.testing as tm
from hypothesis import given
import challenges.ChangeDependingOnOthers.submission as submission

import importlib
importlib.reload(submission)

@given(**ChangeDependingOnOthers.create_df_func())
def test_transform(df):
    expected_df = ChangeDependingOnOthers.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
