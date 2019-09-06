import math

n = int(input())

supLimit = math.floor(math.sqrt(n)) + 1

totalSum = 0

if n == 1:
    totalSum = 1
elif n < 9:
    totalSum = n + math.floor(n/2) - 1
else:
    for i in range(1, supLimit):
        totalSum += (math.floor(n/i) - (i-1))

print(totalSum)