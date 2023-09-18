def is_armstrong_number(number):
    str_number = str(number)
    return number == sum([int(a) ** len(str_number) for a in str_number])
