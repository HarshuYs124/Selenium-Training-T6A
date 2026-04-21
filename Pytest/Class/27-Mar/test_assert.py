
import pytest
def test_equality():
    # assert 5==5 , "not equal"
    assert 4!= 5, "not equal"

def test_equal():
    assert 'hello' == "hello"


@pytest.mark.regression
def test_equallist1():
    list1 = ['apple','banana','mango']
    assert 'apple'in list1
def test_equallist2():
    list1 = ['apple','banana','mango']
    assert 'grapes' not in list1