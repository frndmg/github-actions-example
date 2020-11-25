import argparse
from itertools import islice

from .primes import primes


def take(n, xs):
    return islice(xs, n)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'n', type=int, help='how many primes you want',
    )

    args = parser.parse_args()

    print(
        '\n'.join(
            map(str, take(args.n, primes()))
        )
    )


if __name__ == '__main__':
    main()
