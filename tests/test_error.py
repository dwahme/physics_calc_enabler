from physics import error
import pytest

def test_average_0():
    vals = [0, 1, 2]

    ave = error.average(vals)

    assert ave == 1

def test_average_1():
    vals = [12, 3, 7, 6]

    ave = error.average(vals)

    assert ave == 7

def test_average_single():
    vals = [5]

    ave = error.average(vals)

    assert ave == 5

def test_average_empty():
    vals = []

    with pytest.raises(ValueError):
        error.average(vals)

def test_percent_diff_0():
    expect = 1
    actual = 1

    diff = error.percent_diff(expect, actual)

    assert diff == 0

def test_percent_diff_1():
    expect = 4
    actual = 5

    diff = error.percent_diff(expect, actual)

    assert diff == .2

def test_percent_diff_2():
    expect = 14
    actual = 6

    diff = error.percent_diff(expect, actual)

    assert diff == 8 / 14

def test_percent_diff_error():
    expect = 0
    actual = 3

    with pytest.raises(ZeroDivisionError):
        error.percent_diff(expect, actual)
