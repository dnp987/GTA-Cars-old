'''
Created on May 26, 2020

@author: Home
'''
import pytest
class TestClass:
    def test_one(self):
        x = "this"
        assert "x" in x
    
    def test_two(self):
        x = "hello"
        assert x == "hello"