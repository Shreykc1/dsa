def userinput(rows, cols):
	arr = [[0 for i in range(rows)] for j in range(cols)]
	for i in range(rows):
		for j in range(cols):
			arr[i][j] = int(input("Enter no. "))
	print()
	return arr

def add(m1,m2):
    rows = len(m1)
    cols = len(m1[0])
    
    matrix = [[0 for i in range(rows)] for j in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = m1[i][j] + m2[i][j]
    return matrix


def multiply(m1,m2):
    result = [[0 for i in range(len(m1))] for j in range(len(m2))]
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result



r = int(input("Enter no. of rows: "))
c = int(input("Enter no. of cols: "))
m1 = userinput(r,c)
m2 = userinput(r,c)

m3 = add(m1, m2)
print(m3)