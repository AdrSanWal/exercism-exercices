def sum_of_multiples(limit, multiples):
    result = set()
    values = multiples[:]
    for i, value in enumerate(values):
        if value:
            while value < limit:
                result.add(value)
                value += multiples[i]
    return sum(result)
