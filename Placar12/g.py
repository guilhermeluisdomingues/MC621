def is_prime():
    prime = [True] * 1000000
    prime[0] = False 
    prime[1] = False
    for i in range(2,1000000):
        if prime[i] == True:
            for j in range(i*i, 1000000, i):
                prime[j] = False
    return prime                    

def is_tprime(n):
    if n == 4:
        return True
    if n < 4 or n%2==0:
        return False
    raiz = n**0.5
    if raiz==int(raiz):
        if is_prime[int(raiz)] == True:
            return True
    return False

is_prime = is_prime()
total_numbers = int(input())
numbers = [int(k) for k in input().split()]
for i in numbers:
    if is_tprime(i)==False:
        print("NO")
    else:
        print("YES")