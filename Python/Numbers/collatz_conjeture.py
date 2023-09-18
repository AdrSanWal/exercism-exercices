def steps(number, counter=0):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        counter += 1
        if number % 2 == 0:
            return steps(number / 2, counter)
        else:
            return steps(number * 3 + 1, counter)
    return counter
