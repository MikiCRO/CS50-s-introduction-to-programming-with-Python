import pytest
import um
from um import count

def test_um():
    assert count(" um ") == 1

def test_punct():
    assert count("um?") == 1

def test_long():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    
def test_words():
    assert count("Instrumenatation") == 0