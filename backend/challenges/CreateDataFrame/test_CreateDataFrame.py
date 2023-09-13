# This is sent to the client for testing
#

from challenges.CreateDataFrame.CreateDataFrame import (
    CreateDataFrame,
)
import pandas.testing as tm
from hypothesis import given
import challenges.CreateDataFrame.submission as submission

import importlib
importlib.reload(submission)

@given(**CreateDataFrame.create_df_func())
def test_transform(list1, list2, list3):
    expected_df = CreateDataFrame.transform(list1, list2, list3)
    user_df = submission.transform(list1, list2, list3)
    tm.assert_frame_equal(user_df, expected_df)

