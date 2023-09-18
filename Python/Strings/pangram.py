def is_pangram(sentence):
    letters = list(map(lambda x: chr(x), list(range(122, 96, -1))))
    sentence_letters = sorted(set(sentence.lower()), reverse=True)
    return letters == sentence_letters[:26]
