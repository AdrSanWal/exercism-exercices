from collections import Counter


def is_isogram(string):
    for letter in (c := Counter(string.lower())):
        if letter.isalpha() and c[letter] != 1:
            return False
    return True
