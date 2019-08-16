fibonacci_array = [0,1]
for i in range(2, 60):
    fibonacci_array.append(fibonacci_array[i-1] + fibonacci_array[i-2])

numberOfLoops = int(input())

for i in range(numberOfLoops):
    inputedNumber = int(input())
    if inputedNumber > 5:
        inpNumIndex = fibonacci_array.index(inputedNumber)
        a1 = inpNumIndex - 1    # numero anterior
        a2 = inpNumIndex - 3    # segundo numero anterior
        a3 = inpNumIndex - 4    # terceiro numero anterior
        print(str(fibonacci_array[a3]) + " " + str(fibonacci_array[a2]) + " " + str(fibonacci_array[a1]))
    else:
        print("impossible")