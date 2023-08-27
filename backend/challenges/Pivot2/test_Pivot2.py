# This is sent to the client for testing
#

from challenges.Pivot2.Pivot2 import (
    Pivot2,
)
import pandas.testing as tm
from hypothesis import given
import challenges.Pivot2.submission as submission

import importlib
importlib.reload(submission)

@given(**Pivot2.create_df_func())
def test_transform(df):
    expected_df = Pivot2.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
