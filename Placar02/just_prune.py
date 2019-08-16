numOfLoops = int(input())

for index in range(numOfLoops):
    arrayLenght = input().split(" ")

    inpArray = input().split(" ") + input().split(" ")
    filteredArray = set([x for x in inpArray if inpArray.count(x)%2 != 0])
    print(len(filteredArray))

    # inpArray.sort()
    
    # tst = 0
    # controlArray = [0] * (int(arrayLenght[0]) + int(arrayLenght[1]))
    # for x in inpArray:
    #     controlArray[int(x)] = controlArray[int(x)] + 1

    # mod_sums = [s % 2 for s in controlArray]
    # print(mod_sums.count(1))
