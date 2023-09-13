# This is sent to the client for testing
#

from challenges.CreateDataFrameFromArray.CreateDataFrameFromArray import (
    CreateDataFrameFromArray,
)
import pandas.testing as tm
from hypothesis import given
import challenges.CreateDataFrameFromArray.submission as submission

import importlib
importlib.reload(submission)

@given(**CreateDataFrameFromArray.create_df_func())
def test_transform(array):
    expected_df = CreateDataFrameFromArray.transform(array)
    user_df = submission.transform(array)
    tm.assert_frame_equal(user_df, expected_df)

