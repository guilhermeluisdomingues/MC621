numOfSets = int(input())

for i in range(numOfSets):
    numOfDays = int(input())
    sells = input().split(" ")

    minimum = int(sells[numOfDays-1])
    badDays = 0

    if numOfDays == 1:
        print("0")
    else:
        for i in reversed(sells):
            if(int(i) > int(minimum)):
                badDays += 1
            else:
                minimum = i

        print(badDays)