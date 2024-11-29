matrix1 = [[2,1],
           [5,2]]

matrix2 = [[4,2],
           [1,2]]

result = [[0,0],
          [0,0]]

for i in range(2):
    for j in range(2):
        result[i][j] = (matrix1[i][0] * matrix2[0][j] +
                        matrix1[i][1] * matrix2[1][j])


for row in result:
    print(row)