# This is sent to the client for testing
#

from challenges.TransformWithConditions.TransformWithConditions import (
    TransformWithConditions,
)
import pandas.testing as tm
from hypothesis import given
from challenges.TransformWithConditions.submission import transform

@given(**TransformWithConditions.create_df_func())
def test_transform(df):
    expected_df = TransformWithConditions.transform(df)
    user_df = transform(df)
    assert tm.assert_frame_equal(user_df, expected_df)