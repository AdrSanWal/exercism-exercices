def saddle_points(matrix):
    points = []
    t_matrix = list(zip(*matrix))
    length_row = 0
    for r, row in enumerate(matrix):
        if length_row and len(row) != length_row:
            raise ValueError("irregular matrix")
        length_row = len(row)
        maxium = max(row)
        idx_of_maxiums = [i for i, val in enumerate(row) if val == maxium]
        for c in idx_of_maxiums:
            if row[c] == min(t_matrix[c]):
                points.append({'row': r + 1, 'column': c + 1})
    return points
