n = int(input())

for i in range(0,n):
    line = str(input())

    if line[len(line)-2:len(line)] == '35':
        print('-')
    elif line[0] == '9' and line[len(line)-1] == '4':
        print('*')
    elif line[0:3] == '190':
        print('?')
    else:
        print('+')