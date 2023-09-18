def score(x, y):
    dist = (x ** 2 + y ** 2) ** 0.5
    return 10 if dist <= 1 else 5 if dist <= 5 else 1 if dist <= 10 else 0
