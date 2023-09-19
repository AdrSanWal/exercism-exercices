code = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
        'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}


def label(colors):
    n1, n2, zeros, *_ = map(lambda x: code[x], colors)
    sufix = 'smho ' + int(zeros) * '0'
    number_prev = f'{sufix}{str(int(n1 + n2))[::-1]}'
    s = number_prev.replace(' 000000000', 'agig ')
    s = s.replace(' 000000', 'agem ').replace(' 000', 'olik ')
    return s[::-1]
