import pandas as pd
import numpy as np


df_trusted = pd.DataFrame(
    [
        ["Las Vegas", 650_000],
        ["Tokyo", 13_900_000],
        ["Berlin", -1],  # Unfortunately, this dataframe has no information for Berlin
    ], columns=["city", "inhabitants"]
)
df_noisy = pd.DataFrame(
    [
        ["Berlin", 3_800_000],  # This is noisy. Berlin has 3_700_000 inhabitants
        ["Tokyo", 14_900_000]   # This is noisy. Tokyo has 13_900_000 inhabitants
    ], columns=["city", "inhabitants"]
)

def transform(df_trusted: pd.DataFrame, df_noisy: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
