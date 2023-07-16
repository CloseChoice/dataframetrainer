import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        (1, 1, "term1"),
        (1, 2, "term2"),
        (1, 1, "term1"),
        (1, 1, "term2"),
        (2, 2, "term3"),
        (2, 3, "term1"),
        (2, 2, "term1"),
    ],
    columns=["id", "group", "term"],
)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
