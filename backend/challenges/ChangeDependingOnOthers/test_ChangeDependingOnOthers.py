# This is sent to the client for testing
#

from challenges.ChangeDependingOnOthers.ChangeDependingOnOthers import (
    ChangeDependingOnOthers,
)
import pandas.testing as tm
from hypothesis import given
from challenges.ChangeDependingOnOthers.submission import transform

@given(**ChangeDependingOnOthers.create_df_func())
def test_transform(df):
    expected_df = ChangeDependingOnOthers.transform(df)
    user_df = transform(df)
    assert tm.assert_frame_equal(user_df, expected_df)
