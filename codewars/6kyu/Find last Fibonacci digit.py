def last_fib_digit(n):
    n = n % 60
    if n <= 2:
        if n == 0:
            return 0
        else:
            return 1

    else:
        prev, prev_prev = (1, 1)
        for _ in range(2, n):
            current = (prev + prev_prev) % 10
            prev_prev = prev
            prev = current

        return current
