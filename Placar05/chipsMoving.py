numOfChips = int(input())

chips = input().split(" ")

odd = 0
even = 0

for i in chips:
    if(int(i)%2 == 0):
        odd += 1
    else:
        even += 1

print(min(odd, even))
