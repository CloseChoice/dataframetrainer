# This is sent to the client for testing
#

from challenges.Pivot1.Pivot1 import (
    Pivot1,
)
import pandas.testing as tm
from hypothesis import given
from challenges.Pivot1.submission import transform

@given(**Pivot1.create_df_func())
def test_transform(df):
    expected_df = Pivot1.transform(df)
    user_df = transform(df)
    tm.assert_frame_equal(user_df, expected_df)
