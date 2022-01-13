import math


def divisor_generator(n):
    """
    creating divisors of a sum of values
    """
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i, int(n / i)
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor), int(n / divisor)


def find(lst, a):
    """
    filter divisors lower than out value
    """
    return [(x[0] - 1, x[1] - 1) for x in lst if (x[0] < a) and (x[1] < a)]


def remov_nb(n):
    """
    use a fact that Sum X + 1 = (a + 1) * (b + 1) to find an answer
    """
    result = []
    target = sum(list(range(n + 1)))

    list_of_divisors = list(divisor_generator(target + 1))
    if len(list_of_divisors) > 0:
        result = find(list(divisor_generator(target + 1)), n + 1)
    return result


print(remov_nb(101))
