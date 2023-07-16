# run with
# flask --app server run
from flask import Flask, Response, jsonify
import psycopg2
import sys
from hypothesis.extra.pandas import data_frames, column, indexes
import hypothesis.strategies as st
import json
import numpy as np
import pandas as pd
from flask_cors import CORS, cross_origin

from hypothesis.extra.pandas import data_frames, column, range_indexes, series
from hypothesis.extra.numpy import arrays
from pandas.tseries.offsets import DateOffset
import hypothesis.strategies as st
import os
import time
from flask import send_from_directory

app = Flask(__name__)
CORS(app, support_credentials=True)
app.debug = True


@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
    return jsonify({"success": "ok"})


def check_ping(hostname):
    while True:
        print("Checking network connection...")
        response = os.system("ping -c 1 " + hostname)
        # and then check the response...
        if response == 0:
            print("ping received")
            # sleep for 3 seconds so that db has time to set up
            time.sleep(3)
            return
        time.sleep(5)


host = "db"
# conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='test1234', port=5433)
check_ping(host)
# conn = psycopg2.connect(
#     host=host, dbname="postgres", user="postgres", password="secret", port=5432
# )
conn = psycopg2.connect(
    host=host, dbname="postgres", user="postgres", password="example", port=5432
)
cursor = conn.cursor()


def extract_transform_and_apply(df, transform_string):
    exec(transform_string)
    print(
        f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}"
    )
    return locals()["transform"](df)


@app.route("/", methods=["GET"])
@cross_origin(supports_credentials=True)
def site_response():
    return jsonify({"success": "ok"})


@app.route("/get_challenge/<string:id>/", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_challenge(id):
    return send_from_directory(f"challenges/{id}", f"{id}.py")


@app.route("/get_intro/<string:id>/", methods=["GET"])
def get_intro(id):
    return send_from_directory(f"challenges/{id}", f"intro.md")


@app.route("/get_default/<string:id>/", methods=["GET"])
def get_default(id):
    return send_from_directory(f"challenges/{id}", f"defaultCode.py")


@app.route("/get_all_challenges/", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_all_challenges():
    cursor.execute(f"select id from challenges")
    result = cursor.fetchall()
    return json.dumps([k[0] for k in result])


@app.route("/challenges/<int:id>/", methods=["GET"])
@cross_origin(supports_credentials=True)
def hello(id):
    cursor.execute(f"select * from challenges where id = {id}")
    result = cursor.fetchall()
    # evaluate the string expression to be able to call .example()
    # .example creates an example from the dataframe
    print(result)
    exec(result[0][1])
    df = locals()["initial"]()
    # in result[0][2] there is a function definition like
    # def transform:
    #     df[1] = df[1] + 2
    #     return df
    # this definition will be called with `exec`
    print("\n\n")
    print("This is result[0][2]")
    print(f"{result[0][2]}")
    print(
        f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}"
    )
    exec(result[0][2])
    # transform is now defined and acted upon df
    exec(result[0][3])
    exec(result[0][4])
    df_static = locals()["static_example"]()
    df_static_expected = locals()["expected_static"]()
    df_transformed = extract_transform_and_apply(df, result[0][2])
    print(df)
    print(df_transformed)
    json_response = {
        "initial": df.to_json(),
        "expected": df_transformed.to_json(),
        "static_example": df_static.to_json(),
        "expected_static": df_static_expected.to_json(),
    }
    return jsonify(response=json_response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
