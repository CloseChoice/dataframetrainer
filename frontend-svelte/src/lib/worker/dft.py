import importlib
from importlib import reload
import pytest
import json
import os



def test_code(challenge_name):
    test_module = importlib.import_module(f"challenges.{challenge_name}.test_{challenge_name}")
    submission_module = importlib.import_module(f"challenges.{challenge_name}.submission")

    reload(submission_module)
    reload(test_module)

    pytest.main([
        '--json-report', 
        '--json-report-file' ,'report.json', 
        '--capture=tee-sys',
        f'challenges/{challenge_name}'])
    with open('report.json','r') as file:
        reportContent = file.read()
        return reportContent

def run_code(challenge_name):
    submission_module = importlib.import_module(f"challenges.{challenge_name}.submission")
    challenge_module = importlib.import_module(f"challenges.{challenge_name}.{challenge_name}")
    challenge_class = getattr(challenge_module, challenge_name)
    reload(submission_module)

    params_dict = challenge_class.create_df_func()
    params = _get_params(params_dict)
    submission_module.transform(**params)

def _get_params(paramGeneratorDict):
    return {key: generator.example() for (key, generator) in paramGeneratorDict.items()}

def to_html(object):
    try:
        res = object._repr_html_()
    except:
        res = object.__repr__()
    return res

def generate_example(challenge_name: str) -> str:
    challenge_module = importlib.import_module(f"challenges.{challenge_name}.{challenge_name}")
    challenge_class = getattr(challenge_module, challenge_name)
    params_dict = challenge_class.create_df_func()
    params = _get_params(params_dict)
    params_html = {key: to_html(val) for (key, val) in params.items()}
    result = challenge_class.transform(**params)
    result_html = to_html(result)
    
    return json.dumps({
        "result": result_html,
        "params": params_html
    })
