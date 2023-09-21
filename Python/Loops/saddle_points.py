import numpy as np


def saddle_points(matrix):
    points = []
    for row in matrix:
        maxium = max(row)
        idx_of_maxiums = [i for i, val in enumerate(row) if val == maxium]

    return points


matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
print(saddle_points(matrix))

# [4, 5, 4]
# [3, 5, 5]
# [1, 5, 4]

# [{"row": 1, "column": 2}, {"row": 2, "column": 2}, {"row": 3, "column": 2},]

matrix = []
print(saddle_points(matrix))
