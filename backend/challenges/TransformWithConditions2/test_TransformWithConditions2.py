# This is sent to the client for testing
#

from challenges.TransformWithConditions2.TransformWithConditions2 import (
    TransformWithConditions2,
)
import pandas.testing as tm
from hypothesis import given
import challenges.TransformWithConditions2.submission as submission

import importlib
importlib.reload(submission)

@given(**TransformWithConditions2.create_df_func())
def test_transform(df):
    expected_df = TransformWithConditions2.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
