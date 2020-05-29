"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.

YACHT = ('match', r"1{5}|2{5}|3{5}|4{5}|5{5}|6{5}", 50)
ONES = ('num', 1)
TWOS = ('num', 2)
THREES = ('num', 3)
FOURS = ('num', 4)
FIVES = ('num', 5)
SIXES = ('num', 6)
FULL_HOUSE = ('fh', r"1{5}|2{5}|3{5}|4{5}|5{5}|6{5}")
FOUR_OF_A_KIND = ('four', r"1{4}|2{4}|3{4}|4{4}|5{4}|6{4}")
LITTLE_STRAIGHT = ('match', r"12345", 30)
BIG_STRAIGHT = ('match', r"23456", 30)
CHOICE = ('sum',)


def score(dice, category):
    if category[0] == 'num':
        q = 0
        for i in dice:
            if i == category[1]:
                q += i
        return q
    elif category[0] == 'sum':
        return sum(dice)
    elif category[0] == 'match' or category[0] == 'four':
        import re
        x = ''.join([str(i) for i in sorted(dice)])
        if re.search(category[1], x):
            if category[0] == 'match':
                return category[2]
            return int(x[2]) * 4
        return 0
    elif category[0] == 'fh':
        counts = dict()
        for i in dice:
            counts[i] = counts.get(i, 0) + 1
        freq = (sorted([(v, k) for k, v in counts.items()], reverse=True)[:2])
        if len(freq) >= 2 and freq[0][0] >= 3 and freq[1][0] >= 2:
            return freq[0][1] * 3 + freq[1][1] * 2
        return 0

    return 0
