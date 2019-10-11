stringA = input()
stringB = input()

def lcs(strA, strB, lenA, lenB): 
  
    if lenA == 0 or lenB == 0: 
       return 0; 
    elif strA[lenA-1] == strB[lenB-1]: 
       return 1 + lcs(strA, strB, lenA-1, lenB-1)
    else: 
       return max(lcs(strA, strB, lenA, lenB-1), lcs(strA, strB, lenA-1, lenB))

print(lcs(stringA, stringB, len(stringA), len(stringB)))