import pytest
import working
from working import convert

def test_duljina():
    assert convert("8:00 AM to 9:00 PM")=="08:00 to 21:00"
    assert convert("7:00 AM to 11:00 PM")=="07:00 to 23:00"


    with pytest.raises(ValueError):
        convert("8:00 AM - 9:00 PM")
        convert("8:60 AM to 9:60 PM")
        convert("9:7 AM to 8:00 PM")
        convert("8:66 PM to 5:1 PM")
        convert("9 AM - 5PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 9:60 PM")
    with pytest.raises(ValueError):
        convert("8:66 AM to 5:1 PM")