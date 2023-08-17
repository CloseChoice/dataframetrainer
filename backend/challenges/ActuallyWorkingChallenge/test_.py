# This is sent to the client for testing
#

from challenge import Challenge
import pandas.testing as tm
from hypothesis import given
from submission import transform

@given(**Challenge.create_df_func())
def test_transform(df):
    expected_df = Challenge.transform(df)
    user_df = transform(df)
    tm.assert_frame_equal(user_df, expected_df)
