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

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='test1234', port=5433)
cursor = conn.cursor()

def extract_transform_and_apply(df, transform_string):
    exec(transform_string)
    print(f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}")
    return locals()['transform'](df)

@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def site_response():
  return jsonify({'success': 'ok'})

@app.route('/challenges/<int:id>/', methods=['GET'])
@cross_origin(supports_credentials=True)
def hello(id):
    cursor.execute(f"select * from challenges where id = {id}")
    result = cursor.fetchall()
    # evaluate the string expression to be able to call .example()
    # .example creates an example from the dataframe
    print(result)
    df = eval(result[0][1]).example()
    # in result[0][2] there is a function definition like
    # def transform: 
    #     df[1] = df[1] + 2
    #     return df
    # this definition will be called with `exec`
    print("\n\n")
    print("This is result[0][2]")
    print(f"{result[0][2]}")
    print(f"Try to get locals().get('transform', 'not found'): {locals().get('transform', 'not found')}")
    exec(result[0][2])
    # transform is now defined and acted upon df
    df_transformed = extract_transform_and_apply(df, result[0][2])
    json_response = {"initial": df.to_json(), "expected": df_transformed.to_json()}
    return jsonify(response=json_response)