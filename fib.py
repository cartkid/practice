import sys

cached_fib: dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n <= 0:
        return 0
    sys.setrecursionlimit(100000)
    if n in cached_fib:
        return cached_fib[n]
    result = fib(n - 1) + fib(n - 2)
    cached_fib[n] = result
    return result
