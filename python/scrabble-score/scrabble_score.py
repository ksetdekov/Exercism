def score(word):
    converter = dict.fromkeys(['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'], 1)
    converter.update(dict.fromkeys(['d', 'g'], 2))
    converter.update(dict.fromkeys(['b', 'c', 'm', 'p'], 3))
    converter.update(dict.fromkeys(['f', 'h', 'v', 'w', 'y'], 4))
    converter.update({'k': 5})
    converter.update(dict.fromkeys(['j', 'x'], 8))
    converter.update(dict.fromkeys(['q', 'z'], 10))
    output = 0
    for i in word.lower():
        output += converter[i]
    return output
