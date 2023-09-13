import pandas as pd
import numpy as np
import uuid

df = pd.DataFrame(
    [
        ["Friedrich", "friedrich@gmail.com", uuid.UUID('8c158bf2-4caa-45b3-8c21-ec657411d568'), "Germany"],
        ["Astrid", "astrid@yahoooooo.net", uuid.UUID('ddfc6587-6c07-42b5-a85b-2f92730490a8'), "Sweden"],
        ["Emily", "emily@myowndomain.fr", uuid.UUID('776b9365-f460-47d5-8ced-93e87b7e7ae6'), "France",
        ["Felix", "helmut@justusingmybrothers.uk.co", uuid.UUID('ecb37f92-4ad9-452c-89fc-c705069b3397'), "United States"]]
    ],
    columns=["customerName", "customerEmail", "customerId", "country"],
)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # once you found a solution, define this function
    pass
