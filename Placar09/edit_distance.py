while(True):
    try:
        inputedLine = input()
        even = 0
        odd = 0
        for i in  range(len(inputedLine)):
            if((i % 2) != 0):
                if(inputedLine[i].isupper()):
                    even = even +1
                else: 
                    odd = odd +1
            else:
                if(inputedLine[i].islower()):
                   even = even + 1
                else: 
                  odd = odd + 1
                    
        print(min(even,odd))
    except EOFError:
        break