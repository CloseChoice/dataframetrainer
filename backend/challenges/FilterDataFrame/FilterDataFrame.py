"""Change the a column if its value fulfills a condition. If the Value column is greater than 3, set it to 100, else leave it as is."""
import pandas as pd
import numpy as np
from collections.abc import Callable
from hypothesis.extra.pandas import data_frames, column, indexes, range_indexes

import uuid
import hypothesis.strategies as st

LIST_OF_NAMES = ["James", "Mary"
                 "Robert", "Patricia"
                 "John", "Jennifer"
                 "Michael", "Linda"
                 "David", "Elizabeth"
                 "William", "Barbara"
                 "Richard", "Susan"
                 "Joseph", "Jessica"
                 "Thomas", "Sarah"
                 "Christopher", "Karen"
                 "Charles", "Lisa"
                 "Daniel", "Nancy"
                 "Matthew", "Betty"
                 "Anthony", "Sandra"
                 "Mark", "Margaret"
                 "Donald", "Ashley"
                 "Steven", "Kimberly"
                 "Andrew", "Emily"
                 "Paul", "Donna"
                 "Joshua", "Michelle"]

COUNTRIES = ["Germany", "Denmark", "Sweden", "Italy", "United States", "Canada", "France", "Spain", "Portugal", "Russia"]

class FilterDataFrame:
    @staticmethod
    def create_df_func() -> dict[str, Callable]:
        return {"df": data_frames(
            columns=[
                column("customerName", dtype=np.dtype(str)),
                column("customerEmail", dtype=np.dtype(str)),
                column("customerId", dtype=np.dtype(uuid.UUID)),
                column("country", dtype=np.dtype(str)),
            ],
            rows=st.tuples(
                st.sampled_from(LIST_OF_NAMES),
                st.emails(),
                st.uuids(),
                st.sampled_from(COUNTRIES),
            ),
            index=range_indexes(min_size=3, max_size=10),
        )}

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        return df[df["country"].isin(["Germany", "Sweden"])][["customerId", "country"]]

    @staticmethod
    def static_example() -> pd.DataFrame:
        df = pd.DataFrame(
            [
                ["Friedrich", "friedrich@gmail.com", uuid.UUID('8c158bf2-4caa-45b3-8c21-ec657411d568'), "Germany"],
                ["Astrid", "astrid@yahoooooo.net", uuid.UUID('ddfc6587-6c07-42b5-a85b-2f92730490a8'), "Sweden"],
                ["Emily", "emily@myowndomain.fr", uuid.UUID('776b9365-f460-47d5-8ced-93e87b7e7ae6'), "France"],
                ["Felix", "helmut@justusingmybrothers.uk.co", uuid.UUID('ecb37f92-4ad9-452c-89fc-c705069b3397'), "United States"]
            ],
            columns=["customerName", "customerEmail", "customerId", "country"],
        )
        return df

    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame(
            [
                ["Friedrich", "Germany"],
                ["Astrid", "Sweden"]
            ],
            columns=["customerName", "country"]
        )