import numpy
row, column = eval(input().replace(" ",","))
elements = eval(input().replace(" ",","))
matrix = [[0 for i in range(column)]for i in range(row)]
ptr = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = elements[ptr]
        ptr += 1
print(matrix)