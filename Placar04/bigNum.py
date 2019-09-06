import math

N = int(input())

for i in range(N):
    num = int(input())
    
    if num <= 1:
        print("1")
    else:
        f = ((num * math.log10(num / math.e) + math.log10(2 * math.pi * num) /2.0))
        print(str(math.floor(f) + 1))
