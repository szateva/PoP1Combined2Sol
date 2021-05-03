import pytest
from question2 import *

def test1():
    assert delete_all(s = 'test', what = 'tst') == 'test'
    
def test2():
    assert delete_all(s = 'test', what = 'test') == ''
    
def test3():
    assert delete_all(s = 'testtttest', what = 'tttt') == 'tesest'

def test4():
    assert delete_all(s = 'testtttettttst', what = 'tttt') == "tesest"

def test5():
    with pytest.raises(ValueError):
        delete_all(12, "aaa")
