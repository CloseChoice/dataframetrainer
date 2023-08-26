# This is sent to the client for testing
#

from challenges.GroupTerms.GroupTerms import (
    GroupTerms,
)
import pandas.testing as tm
from hypothesis import given
import challenges.GroupTerms.submission as submission

import importlib
importlib.reload(submission)

@given(**GroupTerms.create_df_func())
def test_transform(df):
    expected_df = GroupTerms.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
