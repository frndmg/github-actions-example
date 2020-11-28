import pytest
from hypothesis import given
from hypothesis.strategies import integers

from primes import is_prime, Primes


@pytest.fixture
def primes():
    return Primes()


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)


def test_primes_getitem(primes):
    assert primes[0] == 2
    assert primes[1] == 3
    assert primes[2] == 5
    assert primes[3] == 7
    assert primes[4] == 11


def test_primes_contains(primes):
    assert 2 in primes
    assert 3 in primes
    assert 4 not in primes
    assert 5 in primes
    assert 6 not in primes


def test_primes_slice(primes):
    a, b, c, d, e = primes[:5]

    assert a == 2
    assert b == 3
    assert c == 5
    assert d == 7
    assert e == 11


def test_error(primes):
    with pytest.raises(TypeError):
        _ = primes['index']


@given(integers(0, 1000))
def test_primality(primes, n):
    assert is_prime(primes[n])


@given(integers(2, 1000))
def test_primality2(primes, n):
    assert is_prime(n) == (n in primes)
