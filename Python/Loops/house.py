def verse(num):
    text = [('house', 'Jack built.'),
            ('malt', 'lay in'),
            ('rat', 'ate'),
            ('cat', 'killed'),
            ('dog', 'worried'),
            ('cow with the crumpled horn', 'tossed'),
            ('maiden all forlorn', 'milked'),
            ('man all tattered and torn', 'kissed'),
            ('priest all shaven and shorn', 'married'),
            ('rooster that crowed in the morn', 'woke'),
            ('farmer sowing his corn', 'kept'),
            ('horse and the hound and the horn', 'belonged to'),
            ]

    result = 'This is'
    for n in range(num - 1, -1, -1):
        result += f' the {text[n][0]} that {text[n][1]}'
    return result


def recite(start_verse, end_verse):
    return [verse(x) for x in range(start_verse, end_verse + 1)]
