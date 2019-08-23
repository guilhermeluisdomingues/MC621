nNumbers = input()
mainArray = input().split(' ')

nQueries = int(input())

for x in range(nQueries):
    queryArray = input().split(' ')

    # if int(queryArray[0]) <= int(queryArray[1]):
    #     subArray = mainArray[int(queryArray[0]) : int(queryArray[1])+1]
    # else:
    #     subArray = mainArray[int(queryArray[1]) : int(queryArray[0])+1]

    subArray = mainArray[int(queryArray[0]) : int(queryArray[1])+1]

    # minValue = int(subArray[0])
    # for i in range(0, len(subArray)):
    #     minValue = int(subArray[i]) if int(subArray[i]) < minValue else minValue

    # print(minValue)

    print(min(subArray))