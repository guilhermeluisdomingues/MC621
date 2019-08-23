
while True:
    try:
        a = int(input())
        b = int(input())
        print(str(a*b))
    except EOFError:
        break