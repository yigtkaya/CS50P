import pytest
from jar import Jar


def test_init():

    jar = Jar(1000, 500)

    assert jar.capacity == 1000
    assert jar.size == 500


    second_jar = Jar()
    assert second_jar.capacity == 12
    assert second_jar.size == 0


def test_capacity():

    fJar = Jar()
    sJar = Jar(123)

    assert fJar.capacity == 12
    assert sJar.capacity == 123

    with pytest.raises(ValueError):
        sJar = Jar(-10)

    with pytest.raises(ValueError):
        fJar = Jar(-1233)

def test_size():

    fJar = Jar(12, 5)
    sJar = Jar(15, 2)

    assert fJar.size == 5
    assert sJar.size == 2

    with pytest.raises(ValueError):

        fJar = Jar(12, -5)

def test_str():
    fJar = Jar(12, 5)
    sJar = Jar(15,6)

    assert str(fJar) == "🍪🍪🍪🍪🍪"
    assert str(sJar) == "🍪🍪🍪🍪🍪🍪"

    fJar.withdraw(3)
    assert str(fJar) == "🍪🍪"

def test_deposit():

    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():

    jar = Jar(12, 3)

    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 4

    jar.withdraw(1)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(5)