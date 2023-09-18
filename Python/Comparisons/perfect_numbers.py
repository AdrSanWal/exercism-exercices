def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    val = sum([a for a in (range(1, number)) if number % a == 0])
    if val == number:
        return 'perfect'
    elif val > number:
        return 'abundant'
    return 'deficient'
