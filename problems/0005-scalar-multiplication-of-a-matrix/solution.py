def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	n=len(matrix)
	m=len(matrix[0])
	for i in range(n):
		for j in range(m):
			matrix[i][j]=scalar*matrix[i][j]
	return matrix
	