# This is sent to the client for testing
#

from challenges.SumSpendings.SumSpendings import (
    SumSpendings,
)
import pandas.testing as tm
from hypothesis import given
import challenges.SumSpendings.submission as submission

import importlib
importlib.reload(submission)

@given(**SumSpendings.create_df_func())
def test_transform(df):
    expected_df = SumSpendings.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
