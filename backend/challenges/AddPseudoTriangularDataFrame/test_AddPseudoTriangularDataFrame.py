# This is sent to the client for testing
#

from challenges.AddPseudoTriangularDataFrame.AddPseudoTriangularDataFrame import (
    AddPseudoTriangularDataFrame,
)
import pandas.testing as tm
from hypothesis import given
from challenges.AddPseudoTriangularDataFrame.submission import transform

@given(**AddPseudoTriangularDataFrame.create_df_func())
def test_transform(df):
    expected_df = AddPseudoTriangularDataFrame.transform(df)
    user_df = transform(df)
    tm.assert_frame_equal(user_df, expected_df)
