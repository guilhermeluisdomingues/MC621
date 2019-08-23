import numpy as np

firstLine = input().split(' ')

matrix = [[0] * int(firstLine[0]) for i in range(int(firstLine[0]))]

for x in range(int(firstLine[1])):
    volcano = input().split(' ')
    matrix[int(volcano[0])][int(volcano[1])] = 1

print(np.matrix(matrix))