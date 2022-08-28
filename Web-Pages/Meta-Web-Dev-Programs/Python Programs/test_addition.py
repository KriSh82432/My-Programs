from audioop import add
import addition
import pytest

def test_add():
    assert addition.add(4, 7) == 11

def test_sub():
    assert addition.sub(4, 3) == 1