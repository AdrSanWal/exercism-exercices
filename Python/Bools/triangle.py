def is_triangle(sides):
    for n in sides:
        if n > sum(sides) - n:
            return False
    return all([_ > 0 for _ in sides])


def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3
