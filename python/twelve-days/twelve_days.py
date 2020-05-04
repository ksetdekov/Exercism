def day(count):
    return ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
            "twelfth"][count - 1]


def recite(start_verse, end_verse):
    for v in range(start_verse, end_verse + 1):
        print(day(v))


for i in range(1, 13):
    recite(i, i)
