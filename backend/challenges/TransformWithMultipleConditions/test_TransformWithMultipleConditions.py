# This is sent to the client for testing
#

from challenges.TransformWithMultipleConditions.TransformWithMultipleConditions import (
    TransformWithMultipleConditions,
)
import pandas.testing as tm
from hypothesis import given
from challenges.TransformWithMultipleConditions.submission import transform

@given(**TransformWithMultipleConditions.create_df_func())
def test_transform(df):
    expected_df = TransformWithMultipleConditions.transform(df)
    user_df = transform(df)
    tm.assert_frame_equal(user_df, expected_df)
