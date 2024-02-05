import pytest
from bank import value

def test_hello():
    assert value("hello")=="0"
    assert value("hi")=="20"
    assert value("Whats up")=="100"