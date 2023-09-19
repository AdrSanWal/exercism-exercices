code = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
        'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
tolerance = {'grey': '0.05', 'violet': '0.1', 'blue': '0.25', 'green': '0.5',
             'brown': '1', 'red': '2', 'gold': '5', 'silver': '10'}


def divide(str_number, divisor):
    number = int(str_number)
    return number / divisor if number % divisor else number // divisor


def resistor_label(colors):
    if colors == ["black"]:
        return "0 ohms"
    t = tolerance[colors.pop()]

    try:
        n1, n2, n3, mult = map(lambda x: code[x], colors)
    except ValueError:
        n3 = ''
        n1, n2, mult = map(lambda x: code[x], colors)

    sufix = 'smho ' + int(mult) * '0'
    number_prev = f'{sufix}{str(int(n1 + n2 + n3))[::-1]}'
    number, unit = number_prev[::-1].split(' ')

    if len(number) > 9:
        return f'{divide(number, 1_000_000_000)} gigaohms ±{t}%'
    elif len(number) > 6:
        return f'{divide(number, 1_000_000)} megaohms ±{t}%'
    elif len(number) > 3:
        return f'{divide(number, 1_000)} kiloohms ±{t}%'
    else:
        return f'{number} ohms ±{t}%'
