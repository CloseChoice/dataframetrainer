"""todo: https://stackoverflow.com/questions/76251529/pandas-transform-with-conditions/76251536#76251536"""
import pandas as pd
import numpy as np
import hypothesis

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
import hypothesis.strategies as st

from BaseChallenge import BaseChallenge

class TransformWithConditions(BaseChallenge):
    @staticmethod
    def initial() -> pd.DataFrame:
        # todo: this is not optimal, but it works for now
        # things to improve: 
        #   - use one of the strategies from hypothesis.extra.pandas to generate the whole df, don't use pd.concat
        #   - length of the df should be variable
        #   - np.nan should be generated in the value column, but this is not possible if one specifies min and max values
        df = data_frames(columns=[column('group', dtype=np.dtype(str)),
                                  column('value', dtype=np.dtype(float)),
                                 ],
                           rows=st.tuples(
                                          st.sampled_from(["A", "B"]),
                                          st.floats(min_value=0., max_value=10., width=16)
                                          ),
                           index=range_indexes(min_size=25, max_size=25)
                         ).example()
        srs = pd.Series(arrays(dtype=np.dtype(int),
                               shape=(25), 
                               elements=st.integers(min_value=1, max_value=25),
                               unique=True).example(), 
                        name='ID', 
                        dtype=np.dtype(int)
                        )
        return pd.concat([srs, df], axis=1)
                    
    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        df['value'] = (df.groupby('group')['value']
                       .transform(lambda x: x.mask(x < 3).ffill().fillna(x.mean())))
        return df
    
    @staticmethod
    def static_example() -> pd.DataFrame:
        return pd.DataFrame({'ID':list(range(1,21)),
            'group': ['A']*10 + ['B']*10,
            'value': [4, 6, 2, 9, 7, 5, 1, 9, 8, 9, np.nan, 4, 5, 6, 1, 2, 3, 4, 2, 6]
            })
    
    @staticmethod
    def expected_static() -> pd.DataFrame:
        return pd.DataFrame([
             [1, "A",  4.000000],
             [2, "A",  6.000000],
             [3, "A",  6.000000],
             [4, "A",  9.000000],
             [5, "A",  7.000000],
             [6, "A",  5.000000],
             [7, "A",  5.000000],
             [8, "A",  9.000000],
             [9, "A",  8.000000],
             [10, "A",  9.000000],
             [11, "B",  3.666667],
             [12, "B",  4.000000],
             [13, "B",  5.000000],
             [14, "B",  6.000000],
             [15, "B",  6.000000],
             [16, "B",  6.000000],
             [17, "B",  3.000000],
             [18, "B",  4.000000],
             [19, "B",  4.000000],
             [20, "B",  6.000000]
            ],
            columns=['ID', 'group', 'value']
        )