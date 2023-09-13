import pandas as pd
import numpy as np
import uuid


uuids = [uuid.UUID('057bdfb8-78fd-4101-8f24-17ac4bba68f8'),
            uuid.UUID('35c8b4fe-deec-4acc-ad25-3850f29137ab'),
            uuid.UUID('0e99d745-26aa-4ba3-8f92-34b54a1a47fa'),
            uuid.UUID('64932494-e446-4d7e-85f7-9039083a03a2')
            ]
df_customer_today = pd.DataFrame(
    [
        [uuids[0], 100],
        [uuids[1], 200]
        [uuids[3], 400]
    ],
    columns=["customerId", "customerSpendings"]
)
df_customer_yesterday = pd.DataFrame(
    [
        [uuids[0], 1000],
        [uuids[1], 2000],
        [uuids[2], 3000]
    ],
    columns=["customerId", "customerSpendings"]
)

def transform(df_customer_today: pd.DataFrame, df_customer_yesterday: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
