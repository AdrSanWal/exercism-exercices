def roman(number, n=''):
    roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
             90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    while roman:
        r = roman.popitem()
        x, _ = divmod(number, r[0])
        number -= (r[0] * x)
        n += r[1] * x
    return n
