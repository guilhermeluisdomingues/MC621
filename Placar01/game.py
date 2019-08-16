# reading input
inputLine = input().split(" ")

n1 = int(inputLine[0])   # player1 balls
n2 = int(inputLine[1])   # p2 balls
k1 = int(inputLine[2])   # p1 taken balls
k2 = int(inputLine[3])   # p2 taken balls

while 1:
    if n1 == 0:
        print("Second")
        exit()

    if n2 == 0:
        print("First")
        exit()

    n1 -= 1
    n2 -= 1