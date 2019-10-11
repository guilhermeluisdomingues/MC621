lenOfInputedCharacter = int(input())
inpCharacter = input()

listOfCharacter = list(set(inpCharacter))
n = len(listOfCharacter)

def compare(filtered):
    for i in range(0, len(filtered) - 1):
        if filtered[i] == filtered[i+1]:
            return False
    return True

maximus = 0
for i in range(0, n - 1):
    for j in range(i+1, n):
        char1 = listOfCharacter[i]
        char2 = listOfCharacter[j]
        
        filtered = list()
        for el in inpCharacter:
            if (el == char1 or el == char2):
                filtered.append(el)

        if compare(filtered):
            maximus = max(maximus, len(filtered))

print(maximus)