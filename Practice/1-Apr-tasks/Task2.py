import pytest

@pytest.mark.smoke
def test_smoke():
    assert 2 + 2 == 4 , "Not Equal"

@pytest.mark.smoke
def test_smoke1():
    assert "welcome".upper() == "WELCOME" , "Not Equal"


@pytest.mark.regression
def test_regression():
    assert 10 > 7 ,"Invalid"

@pytest.mark.regression
def test_regression1():
    list=[1,5,6,3,9]
    assert 6 in list , "Not Equal"