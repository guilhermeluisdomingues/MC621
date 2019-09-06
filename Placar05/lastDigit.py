tCases = int(input())
lastDigOfACases = [1,0,5,6]

for i in range(tCases):
    nums = input().split(" ")
    a = int(nums[0])
    b = int(nums[1])

    lastDigOfA = a%10
    newPower = b%4

    if b == 0:
        print("1")
    elif lastDigOfA in lastDigOfACases or newPower == 1:
        print(lastDigOfA)
    else:
        if newPower == 0:
            print(pow(lastDigOfA, 4)%10)
        else:
            print(pow(lastDigOfA, newPower)%10)