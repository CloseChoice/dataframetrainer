# This is sent to the client for testing
#

from challenges.PivotMedian.PivotMedian import (
    PivotMedian,
)
import pandas.testing as tm
from hypothesis import given
import challenges.PivotMedian.submission as submission

import importlib
importlib.reload(submission)

@given(**PivotMedian.create_df_func())
def test_transform(df):
    expected_df = PivotMedian.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
