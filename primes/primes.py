from itertools import count


def primes():
    cribe = []

    for n in count(2):
        if any(n % p == 0 for p in cribe):
            continue

        yield n
        cribe.append(n)
