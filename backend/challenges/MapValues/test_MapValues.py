# This is sent to the client for testing
#

from challenges.MapValues.MapValues import (
    MapValues,
)
import pandas.testing as tm
from hypothesis import given
import challenges.MapValues.submission as submission

import importlib
importlib.reload(submission)

@given(**MapValues.create_df_func())
def test_transform(df):
    expected_df = MapValues.transform(df.copy(deep=True))
    user_df = submission.transform(df.copy(deep=True))
    tm.assert_frame_equal(user_df, expected_df)

