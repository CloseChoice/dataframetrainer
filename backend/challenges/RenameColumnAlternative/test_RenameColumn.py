# This is just an internal test and is not send to the client
#

from challenges.RenameColumnAlternative.RenameColumnAlternative import RenameColumnAlternative
import pandas as pd
import pandas.testing as tm
from hypothesis import given

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={"Value": "NewValue"})
    return df

@given(df = RenameColumnAlternative.create_df_func())
def test_rename_columns(df):
    expected_df = RenameColumnAlternative.transform(df)
    user_df = transform(df)
    assert tm.assert_frame_equal(user_df, expected_df)
