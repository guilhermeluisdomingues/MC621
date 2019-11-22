row = input().split(" ")

a = [0] * 101
for _ in range(int(row[1])):
    debts = input().split(" ")
    a[int(debts[0])] -= int(debts[2])
    a[int(debts[1])] += int(debts[2])

totalDebts = 0
for i in a:
    if i < 0:
        totalDebts += i

print(str(abs(totalDebts)))