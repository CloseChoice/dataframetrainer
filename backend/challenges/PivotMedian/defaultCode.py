import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        ["Harald", "Groceries", 1],
        ["Harald", "Groceries", 100],
        ["Harald", "Groceries", 1000],
        ["Harald", "Electronics", 20],
        ["Harald", "Entertainment", 20],
        ["Harald", "Entertainment", 400],
        ["Helga", "Entertainment", 20],
        ["Helga", "Groceries", 4],
        ["Friedrich", "Groceries", -1],
        ["Friedrich", "Groceries", 10],
    ],
    columns=["Customer", "Type", "Expense"],
)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
