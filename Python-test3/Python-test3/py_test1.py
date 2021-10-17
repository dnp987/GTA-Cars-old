'''
Created on May 26, 2020

@author: Home
'''
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
