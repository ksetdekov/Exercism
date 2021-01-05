def nth_fib(n):
    if n <= 3:
        if n == 1:
            return 0
        else:
            return 1

    else:
        prev, prev_prev = (1, 1)
        for _ in range(2, n-1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current

        return current
