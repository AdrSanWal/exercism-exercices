def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any([x for x in digits if x < 0 or x >= input_base]):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    digit_len = len(digits)
    n = 0
    for digit in digits:
        digit_len -= 1
        n += digit * (input_base ** digit_len)
    if n == 0:
        return [0]
    result = []
    while n:
        result.append(int(n % output_base))
        n //= output_base
    return result[::-1]
