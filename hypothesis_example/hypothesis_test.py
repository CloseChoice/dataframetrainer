import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.numpy import datetime64_dtypes
from hypothesis.extra.pandas import data_frames, column, indexes
from hypothesis import given
import hypothesis.strategies as st
from datetime import date
import pandas.testing as tm
import ast

df = data_frames(columns=[column('A', dtype=int), column('B', dtype=float)],
                 rows=st.tuples(st.integers(), st.floats(allow_infinity=False, 
                                                         allow_nan=False, 
                                                         allow_subnormal=False))
                ).example()

string = "pd.DataFrame([1, 2, 3], index=range(100, 103))"
import pdb; pdb.set_trace()
given_df = data_frames(columns=[column('ActualDate', dtype=np.dtype('datetime64[ns]'))],
                       index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=1000), dtype=int)
                       )
import pdb; pdb.set_trace()
given_df_string = "data_frames(columns=[column('ActualDate', dtype=np.dtype('datetime64[ns]'))], index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=1000), dtype=int))"
df = eval(given_df_string).example()
import pdb; pdb.set_trace()

# given_df = data_frames(columns=[column('ActualDate', dtype=np.dtype('datetime64[ns]'))],
#                        rows=st.tuples(st.datetimes(min_value=np.datetime64('2000-01-01'),
#                                          max_value=np.datetime64('2030-01-01'))), 
#                        index=indexes(min_size=1, dtype=int)
#                       )
df = given_df.example()

def to_end_of_month(date: date):
    if (date + pd.offsets.Day(1)).month == date.month:
        return date + pd.offsets.MonthEnd(1)
    else:
        return date + pd.offsets.MonthEnd(0)

def transform_bk(df: pd.DataFrame) -> pd.DataFrame:
    df['CalcEnd'] = df['ActualDate'] + pd.offsets.MonthEnd(0)

transform_string = "def transform(df):df['CalcEnd'] = df['ActualDate'] + pd.offsets.MonthEnd(0);return df" 
print(f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}")
exec(transform_string)
print(f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}")
import pdb; pdb.set_trace()

df['CalcEnd'] = df['ActualDate'].apply(to_end_of_month)

@given(df=given_df)
def test_something(df):
    if (df["ActualDate"] < pd.to_datetime("2100-01-01")).all():
        df["CalcEnd"] = df["ActualDate"].apply(to_end_of_month)
        print('executed')
        tm.assert_series_equal(df['CalcEnd'].dt.month, df['ActualDate'].dt.month, check_names=False)
        tm.assert_series_equal(df['CalcEnd'].dt.year, df['ActualDate'].dt.year, check_names=False)
        tm.assert_series_equal(df["CalcEnd"], df['ActualDate'] + pd.offsets.MonthEnd(0), check_names=False)
    

print(df)