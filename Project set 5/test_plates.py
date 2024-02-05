import pytest
import plates
from plates import is_valid

def test_duljina():
    assert is_valid("de345556")==False
    assert is_valid("D")==False
    
def test_prvedvi():
    assert is_valid("34d345")==False
    assert is_valid("3derto")==False
    assert is_valid("de34")==True
    
def test_brojizmedju():
    assert is_valid("de34re")==False
    assert is_valid("der4er")==False
    assert is_valid("deer45")==True
    
def test_cilarijec():
    assert is_valid("alpha")==True
    assert is_valid("34224")==False
