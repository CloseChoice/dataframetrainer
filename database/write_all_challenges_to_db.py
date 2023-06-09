import psycopg2
import sys
from hypothesis.extra.pandas import data_frames, column, indexes
import hypothesis.strategies as st
import numpy as np
import pandas as pd
from challenges.challenge3 import ChangeAtIndex
from challenges.challenge4 import MonthIndex
from challenges.challenge5 import RenameColumn
from challenges.challenge6 import AddTriangularDataFrame
from challenges.challenge7 import AddPseudoTriangularDataFrame
from challenges.challenge8 import GroupTerms
from challenges.challenge9 import MapValues
from challenges.challenge10 import TransformWithConditions
from challenges.challenge11 import TransformWithConditions2
from challenges.challenge12 import TransformWithMultipleConditions
from challenges.challenge13 import GroupbyTransform
from challenges.challenge14 import Pivot1
from challenges.challenge15 import Pivot2
from challenges.compile_challenges import transform_function_string
import inspect
import json
import hypothesis

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
from pandas.tseries.offsets import DateOffset
import hypothesis.strategies as st
import pandas.testing as tm
import click

@click.command()
@click.option('--port', default=5433, help='Port of the database')
@click.option('--password', default="secret", help='Password of the database')
@click.option('--user', default="postgres", help='User of the database')
@click.option('--host', default="localhost", help='Host of the database')
@click.option('--dbname', default="postgres", help='Name of the database')
def run(port, dbname, password, user, host):
    # read the sql file to create challenges
    with open("tables/challenges.sql", "r", encoding="utf-8") as f:
        sql = f.read()
    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
    # conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='secret', port=5434)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("drop table if exists challenges")
    cursor.execute(sql)
    # todo: remove this
    for func in [ChangeAtIndex, MonthIndex, RenameColumn, AddTriangularDataFrame, AddPseudoTriangularDataFrame, 
                 GroupTerms, MapValues, TransformWithConditions, TransformWithConditions2, TransformWithMultipleConditions,
                 GroupbyTransform, Pivot1, Pivot2]:
        print(f"Inserting {func.__name__} into database")
        initial_string = transform_function_string(inspect.getsource(func.initial))
        transform_string = transform_function_string(inspect.getsource(func.transform))
        static_example_func = transform_function_string(inspect.getsource(func.static_example))
        expected_static_func = transform_function_string(inspect.getsource(func.expected_static))
        cursor.execute(f"insert into challenges (initial_task, possible_solution, static_example, expected_static) values ('{initial_string}', '{transform_string}', '{static_example_func}', '{expected_static_func}')")
        # cursor.execute('insert into challenges (initial_task, possible_solution) values ("%s", "%s")', (initial_string, transform_string))
        conn.commit()

        # we test if we can extract the latest challege from the db and execute it
        cursor.execute("select * from challenges where id in (select max(id) from challenges)")
        # we test the stuff above from here on to check if everything worked well
        result = cursor.fetchall()
        # create initial function
        exec(result[0][1])
        df = locals()['initial']()
        # create transform function
        exec(result[0][2])
        # create static example function
        exec(result[0][3])
        # create expected static function
        exec(result[0][4])
        df = locals()['static_example']()
        expected = locals()['expected_static']()
        df_transformed = locals()['transform'](df)
        tm.assert_frame_equal(df_transformed, expected, check_names=False)
        print(df_transformed)
        print("It works!\n")

if __name__ == "__main__":
    run()

