def convert(n):

    # 3 Pling
    # 5 Plang
    # 7 Pl0ng

    p1 = False
    p2 = False
    p3 = False
    if (n % 3) == 0:
        p1 = True
    if (n % 5) == 0:
        p2 = True
    if (n % 7) == 0:
        p3 = True
    test = [p1, p2, p3]

    final = not any(test)
    if not any(test):
        final = n

    return final


test2 = [True, True, True]


print("#########################")
print(convert(1))
print(convert(2))
print(convert(3))
print(convert(4))
print(convert(5))
print(convert(6))
print(convert(7))
print(convert(8))
print(convert(9))
print(convert(10))
print(convert(11))
print(convert(12))
print(convert(13))
print(convert(14))
print(convert(15))
print(convert(16))
print(convert(17))
print(convert(18))
print(convert(19))
print(convert(20))
print(convert(21))
