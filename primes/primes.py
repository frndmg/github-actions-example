from functools import partial
from itertools import count, islice
from operator import le


def is_prime(p):
    return all(
        p % k != 0
        for k in range(2, int(p**.5) + 1)
    )


class Primes:

    def __iter__(self):
        sieve = []

        for n in count(2):
            if any(n % p == 0 for p in sieve):
                continue

            yield n
            sieve.append(n)

    def __getitem__(self, n):
        if isinstance(n, slice):
            return islice(self, n.start, n.stop, n.step)
        elif isinstance(n, int):
            return next(islice(self, n, None))
        else:
            raise TypeError(f'{Primes.__name__} indices be integers of slices, not {type(n).__name__}')

    def __contains__(self, n):
        return n == next(
            filter(partial(le, n), self)
        )
