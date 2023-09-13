from challenges.AntiJoinDataFrames2.AntiJoinDataFrames2 import AntiJoinDataFrames2
import pandas as pd


def transform(df_customer_today: pd.DataFrame, df_customer_yesterday: pd.DataFrame) -> pd.DataFrame:
    return AntiJoinDataFrames2.transform(df_customer_today, df_customer_yesterday)