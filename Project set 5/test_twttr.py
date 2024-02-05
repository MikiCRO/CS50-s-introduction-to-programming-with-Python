import pytest
from twttr import shorten

def test_case():
    assert shorten("pineapple")=="pnppl"
    
