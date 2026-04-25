from fuel import convert


def test_value():
    assert convert("4/5") == "80.0%"
    assert convert("4/") == ValueError
    assert convert("/5") == ValueError
    assert convert("45") == ValueError


def test_zero_division():
    assert convert("4/5") == "80.0%"
    assert convert("0/5") == "E"
    assert convert("5/0") == ZeroDivisionError
    assert convert("0/0") == ZeroDivisionError


def test_attribute():
    assert convert("4/5") == "80.0%"
    assert convert(int("5")) == AttributeError
    assert convert(float("5.5")) == AttributeError


def test_return():
    assert convert("4/5") == "80.0%"
    assert convert("5/5") == "F"
    assert convert("7/7") == "F"
    assert convert("0/5") == "E"
    assert convert("0/13") == "E"
    assert convert("5/4") == "Failed"
