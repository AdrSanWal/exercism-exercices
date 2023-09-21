changes = {
    0: {'animal': "fly",
        'phrase': "I don't know why she swallowed the fly. Perhaps she'll die."},
    1: {'animal': 'spider',
        'phrase': "It wriggled and jiggled and tickled inside her."},
    2: {'animal': 'bird',
        'phrase': "How absurd to swallow a bird!",
        'extra': " that wriggled and jiggled and tickled inside her."},
    3: {'animal': 'cat',
        'phrase': "Imagine that, to swallow a cat!"},
    4: {'animal': 'dog',
        'phrase': "What a hog, to swallow a dog!"},
    5: {'animal': 'goat',
        'phrase': "Just opened her throat and swallowed a goat!"},
    6: {'animal': 'cow',
        'phrase': "I don't know how she swallowed a cow!"},
    7: {'animal': 'horse',
        'phrase': "She's dead, of course!"}
}


def verse(number):
    verse = [f"I know an old lady who swallowed a {changes[number - 1]['animal']}."]
    if number - 1:
        verse.append(changes[number - 1]['phrase'])
    if number == 8:
        return verse
    for n in range(number - 1, -1, -1):
        if n:
            verse.extend([f"She swallowed the {changes[n]['animal']} to catch the {changes[n - 1]['animal']}{changes[n].get('extra', '.')}"])
    verse.append(changes[0]['phrase'])

    return verse


def recite(start_verse, end_verse):
    result = []
    for n in range(start_verse, end_verse + 1):
        result.extend(verse(n))
        result.extend([""])
    return result[:-1]
