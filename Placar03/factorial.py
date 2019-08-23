import math

t = int(input())

for x in range(t):
    num = int(input())
    
    counter = 0
    while(num > 1):
        num = math.floor(num/t)
        counter = counter + 1
    
    print(counter)