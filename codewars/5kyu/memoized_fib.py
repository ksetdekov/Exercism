def fibonacci(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)


fibonacci = memoize(fib)
