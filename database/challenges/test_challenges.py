### todo: write a generic script how to test the challenge classes
from challenge1 import SumSpendings
from challenge2 import ChangeDependingOfOthers
from challenge3 import ChangeAtIndex
from challenge4 import MonthIndex
from challenge5 import RenameColumn
from challenge6 import AddTriangularDataFrame
from challenge7 import AddPseudoTriangularDataFrame
import pandas as pd
import pandas.testing as tm
import pytest


def test_challenge1():
    challenge = SumSpendings()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))

def test_challenge2():
    challenge = ChangeDependingOfOthers()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))

def test_challenge3():
    challenge = ChangeAtIndex()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)

def test_challenge4():
    challenge = MonthIndex()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)

def test_challenge5():
    challenge = RenameColumn()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)

def test_challenge6():
    challenge = AddTriangularDataFrame()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)

def test_challenge7():
    challenge = AddPseudoTriangularDataFrame()
    df = challenge.initial()
    df_result = challenge.transform(df)
    assert isinstance(df, pd.DataFrame)
    # check that the transform does anything
    assert isinstance(df_result, (pd.DataFrame, pd.Series))
    df = challenge.static_example()
    df_expected = challenge.expected_static()
    df_result = challenge.transform(df)
    tm.assert_frame_equal(df_result, df_expected)