from calculator import square
import pytest


def test_square():
    assert square(2)==4
    assert square(3)==9
def test_square_negative():   
    assert square(-4)==16
    assert square(-5)==25
def test_square_zero():
    assert square(0)==0
def test_square_str():
    with pytest.raises(TypeError):
        square("cat")
