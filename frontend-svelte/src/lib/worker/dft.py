import importlib
from importlib import reload
import challenge
import submission
import test_
import pytest


def test_code(code):
    reload(submission)
    reload(test_)
    reload(challenge)
    pytest.main(['--json-report', '--json-report-file' ,'report.json', '--capture=tee-sys'])
    with open('report.json','r') as file:
        reportContent = file.read()
        return reportContent
    
# def run_code(code):
