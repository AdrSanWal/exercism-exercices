from re import search


def is_valid(isbn):
    isbn = isbn.replace('-', '')[::-1]
    pattern = r'^[0-9X]{1}\d{9}$'
    if search(pattern, isbn):
        isbn = list(isbn)
        if isbn[0] == 'X':
            isbn[0] = 10
        r = sum([i * int(n) for i, n in enumerate(isbn, 1)]) % 11
        return not bool(r)
    return False
