import pytest
import numb3rs
from numb3rs import validate

def test_duljina():
    assert validate("127.0.0.1")==True
    assert validate("254.254.254.254")==True
    assert validate("400.222.222.222")==False
    assert validate("cat")==False
    
def test_prvibyte():
    assert validate("125")==False