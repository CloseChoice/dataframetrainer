# This is sent to the client for testing
#

from challenges.GroupTerms.GroupTerms import (
    GroupTerms,
)
import pandas.testing as tm
from hypothesis import given
from challenges.GroupTerms.submission import transform

@given(**GroupTerms.create_df_func())
def test_transform(df):
    expected_df = GroupTerms.transform(df)
    user_df = transform(df)
    assert tm.assert_frame_equal(user_df, expected_df)
