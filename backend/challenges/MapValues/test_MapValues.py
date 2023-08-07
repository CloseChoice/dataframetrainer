# This is sent to the client for testing
#

from challenges.MapValues.MapValues import (
    MapValues,
)
import pandas.testing as tm
from hypothesis import given
from challenges.MapValues.submission import transform

@given(**MapValues.create_df_func())
def test_transform(df):
    expected_df = MapValues.transform(df)
    user_df = transform(df)
    tm.assert_frame_equal(user_df, expected_df)
