from functions import *
import pytest

class TestClass():
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert type(x) is str

def test_succ():
    assert succ(0) == 1

def test_factorial():
    assert factorial(5) == 120

def test_factorial_0():
    assert factorial(0) == 1

def test_factorial_neg():
    assert factorial(-100) == ValueError

def test_mean():
    assert mean((1,2,3,4,5)) == 3.0

def test_mean_type():
    assert type(mean([0,2,3,5])) is float

def test_mean_empty():
    with pytest.raises(ZeroDivisionError):
        mean(())

def test_variance_type():
    assert type(variance((0,1,2,3))) == float

def test_variance():
    assert variance((0,1,2,3,4,5,6)) == 4.0

def test_sd_type():
    assert type(sd((0,1,2,3,4))) == float

def test_sd():
    assert sd((0,1,2,3,4,5,6)) == 2.0

def test_divisors():
    assert divisors(10) == (2,5,10)

def test_divisors_0():
    assert divisors(0) == None

def test_divisors_1():
    assert divisors(1) == (1)

def test_divisors_2():
    assert divisors(2) == (2)

def test_divisors_type():
    assert type(divisors(10)) == tuple

def test_isprime():
    assert isprime(53) == True

def test_isntprime():
    assert isprime(10) == False

def test_1isntprime():
    assert isprime(1) == False

def test_2isprime():
    assert isprime(2) == True
