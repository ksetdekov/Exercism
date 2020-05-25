def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-", "")
    counts = dict()
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1
    bigcount = 1
    for wrd, cnt in counts.items():
        if cnt > bigcount:
            bigcount = cnt
    return bigcount == 1
