# This is sent to the client for testing
#

from challenges.SumSpendings.SumSpendings import (
    SumSpendings,
)
import pandas.testing as tm
from hypothesis import given
from challenges.SumSpendings.submission import transform

@given(**SumSpendings.create_df_func())
def test_transform(df):
    expected_df = SumSpendings.transform(df)
    user_df = transform(df)
    tm.assert_series_equal(user_df, expected_df)
