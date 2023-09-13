from challenges.FixConflictingDataFrames.FixConflictingDataFrames import FixConflictingDataFrames
import pandas as pd


def transform(df_customer_today: pd.DataFrame, df_customer_yesterday: pd.DataFrame) -> pd.DataFrame:
    return FixConflictingDataFrames.transform(df_customer_today, df_customer_yesterday)