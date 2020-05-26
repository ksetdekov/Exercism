import re


def abbreviate(words):
    individual = re.findall(r"[A-Z']+", words.upper())
    return ''.join([i[0] for i in individual])
