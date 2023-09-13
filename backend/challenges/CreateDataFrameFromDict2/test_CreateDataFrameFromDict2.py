# This is sent to the client for testing
#

from challenges.CreateDataFrameFromDict2.CreateDataFrameFromDict2 import (
    CreateDataFrameFromDict2,
)
import pandas.testing as tm
from hypothesis import given
import challenges.CreateDataFrameFromDict2.submission as submission

import importlib
importlib.reload(submission)

@given(**CreateDataFrameFromDict2.create_df_func())
def test_transform(data):
    expected_df = CreateDataFrameFromDict2.transform(data)
    user_df = submission.transform(data)
    tm.assert_frame_equal(user_df, expected_df)

