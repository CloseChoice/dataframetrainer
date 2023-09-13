# This is sent to the client for testing
#

from challenges.AntiJoinDataFrames2.AntiJoinDataFrames2 import (
    AntiJoinDataFrames2,
)
import pandas.testing as tm
import pandas as pd
from hypothesis import given
import challenges.AntiJoinDataFrames2.submission as submission

import importlib
importlib.reload(submission)

@given(**AntiJoinDataFrames2.create_df_func())
def test_transform(df_customer_today: pd.DataFrame, df_customer_yesterday: pd.DataFrame):
    expected_df = AntiJoinDataFrames2.transform(df_customer_today, df_customer_yesterday)
    user_df = submission.transform(df_customer_today, df_customer_yesterday)
    tm.assert_frame_equal(user_df.sort_values(list(user_df.columns)).reset_index(drop=True),
                          expected_df.sort_values(list(user_df.columns)).reset_index(drop=True))

