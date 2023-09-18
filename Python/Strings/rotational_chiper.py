def rotate(text, key):
    result = ''
    for letter in text:
        if letter.isalpha():
            n = ord(letter) + key
            pos = {0: 122, 1: 90}
            result += chr(n) if n <= pos[letter.isupper()] else chr(n - 26)
        else:
            result += letter
    return result
