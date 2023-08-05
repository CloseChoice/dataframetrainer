# This is sent to the client for testing
#

from challenges.AddTriangularDataFrame.AddTriangularDataFrame import (
    AddTriangularDataFrame,
)
import pandas.testing as tm
from hypothesis import given
from challenges.AddTriangularDataFrame.submission import transform

@given(**AddTriangularDataFrame.create_df_func())
def test_transform(df):
    expected_df = AddTriangularDataFrame.transform(df)
    user_df = transform(df)
    assert tm.assert_frame_equal(user_df, expected_df)
