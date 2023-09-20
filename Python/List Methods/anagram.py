def find_anagrams(word, candidates):
    w = word.lower()
    candidates = [_ for _ in candidates if _.lower() != w]
    result = [_ for _ in candidates if ''.join(sorted(_.lower())) == ''.join(sorted(w))]

    return result

candidates = ["lemons", "cherry", "melons"]
print(find_anagrams("solemn", candidates))  # ["lemons", "melons"]

candidates = ["banana"]
print(find_anagrams("BANANA", candidates))  # []

candidates = ["Eons", "ONES"]
print(find_anagrams("nose", candidates))  # ["Eons", "ONES"]
