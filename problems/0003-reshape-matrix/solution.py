def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    rows = new_shape[0]
    cols = new_shape[1]

    n = len(a)
    m = len(a[0])

    if rows * cols != n * m:
        return []

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            index = i * cols + j
            old_row = index // m
            old_col = index % m

            row.append(a[old_row][old_col])

        result.append(row)

    return result