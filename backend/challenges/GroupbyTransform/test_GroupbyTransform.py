# This is sent to the client for testing
#

from challenges.GroupbyTransform.GroupbyTransform import (
    GroupbyTransform,
)
import pandas.testing as tm
from hypothesis import given
import challenges.GroupbyTransform.submission as submission

import importlib
importlib.reload(submission)

@given(**GroupbyTransform.create_df_func())
def test_transform(df):
    expected_df = GroupbyTransform.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
