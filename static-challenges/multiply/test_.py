# from hypothesis import given, strategies as st
import solution
from importlib import reload
reload(solution)
from solution import solution
import pytest


def test_multiplication():
    assert solution(2, 5) == 10



if __name__ == "__main__":
    pytest.main()
