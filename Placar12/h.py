n = int(input())
for i in range(n):
    cont1 = 0
    cont2 = 0
    n1 = int(input())
    pi = [int(k) for k in input().split()]
    n2 = int(input())
    qi = [int(k) for k in input().split()]
    for k in range(n1):
        if((pi[k] % 2) == 0):
            cont1 += 1
    for j in range(n2):
        if((qi[j] % 2) == 0):
            cont2 += 1
            
    intersect = cont2*cont1 + (n1 - cont1)*(n2 - cont2)

    print(intersect)