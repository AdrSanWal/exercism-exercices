def square(number):
    grains = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for n in range(1, number):
        grains *= 2
    return grains


def total():
    return square(64) * 2 - 1
