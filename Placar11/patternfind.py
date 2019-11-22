def find_substrings(string, substring):
    res = []
    counter = 0
    while counter < len(string):
        counter = string.find(substring, counter)
        if counter == -1:
            return res
        else:
            res.append(counter+1)
            counter += 1
    return res

numOfRows = int(input())
for _ in range(numOfRows):
    row = input().split()
    array = find_substrings(row[0], row[1])
    
    if(len(array) <= 0):
        print("Not Found")
    else: 
        print(len(array))
        print(*array)