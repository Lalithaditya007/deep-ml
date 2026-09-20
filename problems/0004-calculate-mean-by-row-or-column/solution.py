def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	n=len(matrix)
	m=len(matrix[0])
	ans=[]
	if mode=='column' :
		for i in range(m):
			sum1=0
			for j in range(n):
				sum1+=matrix[j][i]
			ans.append(sum1/n)
	else:
		for i in range(n):
			sum1=0
			for j in range(m):
				sum1+=matrix[i][j]
			ans.append(sum1/m)
	return ans
	

