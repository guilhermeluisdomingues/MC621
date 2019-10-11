import math
def longestPrefixSuffix(s) : 
    n = len(s) 
      
    for res in range(n // 2, 0, -1) : 
          
        prefix = s[0: res] 
        suffix = s[n - res: n] 
          
        if (prefix == suffix) : 
            return res 
              
    return 0

while (1):
    row = input().split(" ")
    length = int(row[0])
    string = row[1]
    lenString = len(string)

    if length == -1: break
    
    if lenString > length:
        print(str(0))
    else:
        prefixLen = longestPrefixSuffix(string)

        tst = math.floor((length - prefixLen) / (lenString - prefixLen))
        print(tst)
        