def divisors(n, m):
    total = 0
    control = 0
    while(control < n):
        if(control%m == 0):
            tst = control % 10
            total += tst
        control += m
    return total

numOfQueries = int(input())

for i in range(numOfQueries + 1):
    numbers = input().split(" ")
    n = int(numbers[0])
    m = int(numbers[1])

    if m > n:
        print("0")
    elif m == 1:
        total = int((n*(n-1))/2)
        print(total)
    else:
        print(str(divisors(n, m)))