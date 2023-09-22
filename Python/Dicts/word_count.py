from re import findall
from collections import Counter


def count_words(sentence):
    pattern = "[a-z]+'[a-z]+|[a-z]+|[0-9]+"
    c = Counter(findall(pattern, sentence.lower()))
    return dict(c)
