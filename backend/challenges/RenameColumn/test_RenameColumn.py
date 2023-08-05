# This is sent to the client for testing
#

from challenges.RenameColumn.RenameColumn import (
    RenameColumn,
)
import pandas.testing as tm
from hypothesis import given
from challenges.RenameColumn.submission import transform

@given(**RenameColumn.create_df_func())
def test_transform(df):
    expected_df = RenameColumn.transform(df)
    user_df = transform(df)
    tm.assert_frame_equal(user_df, expected_df)
