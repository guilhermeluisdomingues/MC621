numOfLoops = int(input())

for index in range(numOfLoops):
    arrayLenght = input().split(" ")

    array1 = input().split(" ")
    array2 = input().split(" ")
    
    array1.sort()
    array2.sort()

    equalEments = 0

    i = 0
    j = 0
    while (i < (int(arrayLenght[0])) and j < (int(arrayLenght[1])) ):
        if (array1[i] == array2[j]):
            equalEments = equalEments + 1
            i = i + 1
            j = j + 1
        else:
            if (array1[i] > array2[j]):
                j = j + 1
            else:
                i = i + 1
    
    totalItens = int(arrayLenght[0]) + int(arrayLenght[1])
   
    totalDiffItens = totalItens - 2*equalEments

    print(str(totalDiffItens))