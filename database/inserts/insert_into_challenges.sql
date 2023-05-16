insert into challenges (id, initial_task, possible_solution) values (1, 
                               '"data_frames(columns=[column(''ActualDate'', dtype=np.dtype(''datetime64[ns]''))], index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=1000), dtype=int))"'::json,
                               '"def transform(df):df[''CalcEnd''] = df[''ActualDate''] + pd.offsets.MonthEnd(0);return df"'::json
                               );

insert into challenges (id, initial_task, possible_solution) values (2, 
                               '"data_frames(columns=[column(''Customer'', dtype=np.dtype(str)), column(''Spendings'', dtype=np.dtype(float)), ], rows=st.tuples(st.sampled_from([''Helmut'', ''Greta'', ''Siegfried'']), st.floats(allow_infinity=False, allow_nan=False, allow_subnormal=False, min_value=0.0, max_value=1000, width=16, exclude_min=True)), index=indexes(min_size=1, elements=st.integers(min_value=1, max_value=20), dtype=int)) "'::json,
                               '"def transform(df): return df.groupby(''Customer'').Spendings.sum()"'::json
                               );