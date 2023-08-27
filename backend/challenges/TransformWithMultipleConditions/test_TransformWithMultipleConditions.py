# This is sent to the client for testing
#

from challenges.TransformWithMultipleConditions.TransformWithMultipleConditions import (
    TransformWithMultipleConditions,
)
import pandas.testing as tm
from hypothesis import given
import challenges.TransformWithMultipleConditions.submission as submission

import importlib
importlib.reload(submission)

@given(**TransformWithMultipleConditions.create_df_func())
def test_transform(df):
    expected_df = TransformWithMultipleConditions.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
