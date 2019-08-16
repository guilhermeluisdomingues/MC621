import numpy

numOfTests = int(input())

for x in range(numOfTests):
    inpt = input().split(" ")
    base = int(inpt[0])
    exp = int(inpt[1])
    mod = int(inpt[2])

    result = pow(base, exp, mod)
    print(str(x+1) + ". " + str(result))
