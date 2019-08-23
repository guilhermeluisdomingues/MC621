inputedNumber = int(input(), 2)

count = 0
mult = 1
while mult < inputedNumber:
    mult = mult * 4
    count = count + 1

print(count)