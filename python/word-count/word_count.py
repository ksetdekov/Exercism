import re


def count_words(sentence):
    words = re.findall(r"[a-z]+'?[a-z]+|[a-z]+|\d+", sentence.lower())
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
