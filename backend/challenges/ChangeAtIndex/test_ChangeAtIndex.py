# This is sent to the client for testing
#

from challenges.ChangeAtIndex.ChangeAtIndex import (
    ChangeAtIndex,
)
import pandas.testing as tm
from hypothesis import given
from challenges.ChangeAtIndex.submission import transform

@given(**ChangeAtIndex.create_df_func())
def test_transform(df):
    expected_df = ChangeAtIndex.transform(df)
    user_df = transform(df)
    assert tm.assert_frame_equal(user_df, expected_df)
