from itertools import islice

from primes import primes


def take(n, xs):
    return islice(xs, n)


def test_first_primes():
    a, b, c, d, e = take(5, primes())

    assert a == 2
    assert b == 3
    assert c == 5
    assert d == 7
    assert e == 11
