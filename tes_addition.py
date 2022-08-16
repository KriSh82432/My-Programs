import addition
import pytest

def test_add():
    assert addition.add(4, 7) == 11
    assert addition.add(7, 2) == 9

def test_sub():
    assert addition.sub(4, 3) == 1
    assert True