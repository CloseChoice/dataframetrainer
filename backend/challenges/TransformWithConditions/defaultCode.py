import pandas as pd
import numpy as np


df = pd.DataFrame(
            {
                "ID": list(range(1, 21)),
                "group": ["A"] * 10 + ["B"] * 10,
                "value": [4, 6, 2, 9, 7, 5, 1, 9, 8, 9, np.nan, 4, 5, 6, 1, 2, 3, 4, 2, 6],
            }
        )


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
