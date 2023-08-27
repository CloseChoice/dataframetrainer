# This is sent to the client for testing
#

from challenges.AddTriangularDataFrame.AddTriangularDataFrame import (
    AddTriangularDataFrame,
)
import pandas.testing as tm
from hypothesis import given
import challenges.AddTriangularDataFrame.submission as submission

import importlib
importlib.reload(submission)


@given(**AddTriangularDataFrame.create_df_func())
def test_transform(df):
    expected_df = AddTriangularDataFrame.transform(df)
    user_df = submission.transform(df)
    tm.assert_frame_equal(user_df, expected_df)
