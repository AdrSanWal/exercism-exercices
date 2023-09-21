def rows(letter):
    r = ord(letter) - 64
    result = []
    for number in range(r):
        file = f"{(r - 1 - number) * ' '}{chr(number + 65)}{' '*number}"
        file += file[-2::-1]
        result.extend([file])
    return result + result[-2::-1]
