import psycopg2
import sys
from hypothesis.extra.pandas import data_frames, column, indexes
import hypothesis.strategies as st
import numpy as np
import pandas as pd

def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='secret' port=5433"

    # print the connection string we will use to connect
    print("Connecting to database\n    ->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    # conn = psycopg2.connect(conn_string)
    import pdb; pdb.set_trace()
    conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='test1234', port=5433)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    import pdb; pdb.set_trace()
    cursor.execute("select * from challenges")
    result = cursor.fetchall()
    df = eval(result[1][1]).example()
    import pdb; pdb.set_trace()
    # define transform
    print(f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}")
    exec(result[1][2])
    print(f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}")
    df_transformed = locals()['transform'](df)
    print(df_transformed)
    print("It works!\n")

if __name__ == "__main__":
    main()