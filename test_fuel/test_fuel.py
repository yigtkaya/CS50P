from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("0/15") == 0
    assert convert("12/24") == 50
    assert convert("1/2") == 50
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_zeroDiv():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_valueError():
    with pytest.raises(ValueError):
        convert("cat/dog")