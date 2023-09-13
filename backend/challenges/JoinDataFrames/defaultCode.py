import pandas as pd
import numpy as np
import uuid

uuids = [uuid.UUID('057bdfb8-78fd-4101-8f24-17ac4bba68f8'),
         uuid.UUID('35c8b4fe-deec-4acc-ad25-3850f29137ab')]
df1 = pd.DataFrame(
    [
        [uuids[0], 100],
        [uuids[1], 200]
    ], columns=["customerId", "customerSpendings"]
)
df2 = pd.DataFrame(
    [
        [uuids[0], "Charles"],
        [uuids[1], "Andrew"]
    ], columns=["customerId", "customerSpendings"]
)


def transform(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
