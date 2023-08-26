# This is sent to the client for testing
#

from challenges.RenameColumn.RenameColumn import (
    RenameColumn,
)
import pandas.testing as tm
from hypothesis import given
import challenges.RenameColumn.submission as submission

import importlib
importlib.reload(submission)

@given(**RenameColumn.create_df_func())
def test_transform(df):
    expected_df = RenameColumn.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
