import pytest


def perkalian(a,b):
    c = a*b
    return c

# def test_perkalian():
#     hasil = perkalian(2,3)

#     assert == 6


#pytest mark parametrize
num = [
    (2,3,6),
    (1,99,99),
    (0,99,0),
    (25,4,100)
]

@pytest.mark.parametrize('a,b,c', num)

def test_perkalian(a,b,c):
    hasil = perkalian(a,b)

    assert hasil == c
