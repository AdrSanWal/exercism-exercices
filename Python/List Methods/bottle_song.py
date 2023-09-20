numbers = {10: 'Ten',
           9: 'Nine',
           8: 'Eight',
           7: 'Seven',
           6: 'Six',
           5: 'Five',
           4: 'Four',
           3: 'Three',
           2: 'Two',
           1: 'One',
           0: 'No'
           }


def verse(num):
    bottles = (lambda x: f"{numbers[x]} green bottle{'s' if x != 1 else ''}")
    start = f"{bottles(num)} hanging on the wall,"
    middle = "And if one green bottle should accidentally fall,"
    end = f"There'll be {bottles(num - 1).lower()} hanging on the wall."
    return [start, start, middle, end]


def recite(start, take=1):
    result = []
    for n in range(start, start - take, -1):
        result.extend(verse(n))
        result.extend([""])
    return result[:-1]
