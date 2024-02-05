import pytest
import seasons
from seasons import get_birthdate 

def test_words():
    
    
   
    with pytest.raises(SystemExit):
        get_birthdate("2012.10.10")
        
    