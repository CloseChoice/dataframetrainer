# This is sent to the client for testing
#

from challenges.CreateDataFrameFromDict.CreateDataFrameFromDict import (
    CreateDataFrameFromDict,
)
import pandas.testing as tm
from hypothesis import given
import challenges.CreateDataFrameFromDict.submission as submission

import importlib
importlib.reload(submission)

@given(**CreateDataFrameFromDict.create_df_func())
def test_transform(data):
    expected_df = CreateDataFrameFromDict.transform(data)
    user_df = submission.transform(data)
    tm.assert_frame_equal(user_df, expected_df)

