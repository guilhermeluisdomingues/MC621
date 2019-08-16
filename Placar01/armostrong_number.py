def verifyNumber(number):
    numberSize = int(len(str(number)))
    
    totalSum = 0
    for i in range(numberSize):
        totalSum += pow(int(number[i]), numberSize)

    if totalSum == int(number):
        print("Armstrong")
    else: 
        print("Not Armstrong")


# reading the numbers
numbersOfInput = int(input())

i = 1
while i < numbersOfInput + 1:
    number = input()
    verifyNumber(number)
    i += 1