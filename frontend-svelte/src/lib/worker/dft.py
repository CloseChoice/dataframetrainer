import importlib
from importlib import reload
import pytest
import challenge
import json

def test_code():
    import submission
    import test_
    reload(submission)
    reload(test_)
    reload(challenge)
    pytest.main(['--json-report', '--json-report-file' ,'report.json', '--capture=tee-sys'])
    with open('report.json','r') as file:
        reportContent = file.read()
        return reportContent

def run_code():
    import submission
    reload(submission)
    params_dict = challenge.Challenge.create_df_func()
    params = _get_params(params_dict)
    submission.transform(**params)

def _get_params(paramGeneratorDict):
    return {key: generator.example() for (key, generator) in paramGeneratorDict.items()}

def to_html(object):
    try:
        res = object._repr_html_()
    except:
        res = object.__repr__()
    return res

def generate_example():
    params_dict = challenge.Challenge.create_df_func()
    params = _get_params(params_dict)
    params_html = {key: to_html(val) for (key, val) in params.items()}
    result = challenge.Challenge.transform(**params)
    result_html = to_html(result)
    
    return json.dumps({
        "result": result_html,
        "params": params_html
    })
# def run_code(code):
