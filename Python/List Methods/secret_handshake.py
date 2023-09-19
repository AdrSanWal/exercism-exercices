def commands(binary_str):
    text = ['jump', 'close your eyes', 'double blink', 'wink']

    if int(binary_str[0]):
        actions = zip(binary_str[1:], text)
    else:
        actions = zip(binary_str[:0:-1], text[::-1])

    return [b for a, b in actions if int(a)]
