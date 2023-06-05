"""Sum the spendings per Customer."""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, indexes
import hypothesis.strategies as st

from .BaseChallenge import BaseChallenge

class SumSpendings(BaseChallenge):
    @staticmethod
    def initial() -> pd.DataFrame:
        return data_frames(columns=[column('Customer', dtype=np.dtype(str)),
                                    column('Spendings', dtype=np.dtype(float)),
                                 ],
                             rows=st.tuples(st.sampled_from(['Helmut', 'Greta', 'Siegfried']), st.floats(allow_infinity=False,
                                                                                                 allow_nan=False,
                                                                                                 allow_subnormal=False,
                                                                                                 min_value=0.0,
                                                                                                 max_value=1000,
                                                                                                 width=16,
                                                                                                 exclude_min=True)),
                          index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=20), dtype=int)
                         ).example()
    @staticmethod
    def transform(df: pd.DataFrame) -> pd.Series:
        return df.groupby('Customer').Spendings.sum()


### SEE: https://stackoverflow.com/a/19850183/9534390 for hints how to compile a string
#  '"data_frames(columns=[column(''Customer'', dtype=np.dtype(str)), 
#                         column(''Spendings'', dtype=np.dtype(float)), 
#                        ], 
#                rows=st.tuples(st.sampled_from([''Helmut'', 
#                                                ''Greta'', 
#                                                ''Siegfried'']), 
#                               st.floats(allow_infinity=False, 
#                                         allow_nan=False, 
#                                         allow_subnormal=False, 
#                                         min_value=0.0, 
#                                         max_value=1000, 
#                                         width=16, 
#                                         exclude_min=True
#                                         )), 
#                               index=indexes(min_size=1, 
#                                             elements=st.integers(min_value=1, 
#                                                                  max_value=20), 
#                                             dtype=int)) "'::json,
#  '"def transform(df): return df.groupby(''Customer'').Spendings.sum()"'::json

# import pandas as pd
# import numpy as np
# import hypothesis
# 
# from hypothesis.extra.numpy import datetime64_dtypes
# from hypothesis.extra.pandas import data_frames, column, indexes
# from hypothesis import given
# import hypothesis.strategies as st
# from datetime import date
# import pandas.testing as tm
# import ast
# 
# 
# df = data_frames(columns=[column('A', dtype=int), column('B', dtype=float)],
#                  rows=st.tuples(st.integers(), st.floats(allow_infinity=False, 
#                                                          allow_nan=False, 
#                                                          allow_subnormal=False))
#                 ).example()
# 
# generate_string = """
# def generate():
#     return data_frames(columns=[column('Customer', dtype=np.dtype(str)),
#                                     column('Spendings', dtype=np.dtype(float)),
#                                 ],
#                             rows=st.tuples(st.sampled_from(["Helmut", "Greta", "Siegfried"]), st.floats(allow_infinity=False,
#                                                                                                 allow_nan=False,
#                                                                                                 allow_subnormal=False,
#                                                                                                 min_value=0.0,
#                                                                                                 max_value=1000,
#                                                                                                 width=16,
#                                                                                                 exclude_min=True)),
#                         index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=20), dtype=int)
#                         )
# """
# 
# 
# given_df = data_frames(columns=[column('Customer', dtype=np.dtype(str)),
#                                 column('Spendings', dtype=np.dtype(float)),
#                                ],
#                         rows=st.tuples(st.sampled_from(["Helmut", "Greta", "Siegfried"]), st.floats(allow_infinity=False,
#                                                                                             allow_nan=False,
#                                                                                             allow_subnormal=False,
#                                                                                             min_value=0.0,
#                                                                                             max_value=1000,
#                                                                                             width=16,
#                                                                                             exclude_min=True)),
#                        index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=20), dtype=int)
#                        )
# generate_compiled = compile(generate_string, '', 'exec')
# import pdb; pdb.set_trace()
# exec(generate_compiled)
# tt = generate().example()
# 
# 
# 
# def transform(df):
#     return df.groupby("Customer").Spendings.sum()
# 
# @given(df=given_df)
# def test_something(df):
#     tm.assert_frame_equal(transform(df), df.groupby(["Customer"]).agg({"Spendings": sum}))
# 