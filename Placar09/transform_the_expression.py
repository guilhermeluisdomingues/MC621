def defPriority(operator, operator2):
  if(operator == '^'):
    priOp = 4
  elif(operator == '*' or operator == '/'):
    priOp = 2
  elif(operator == '+' or operator == '-'):
    priOp = 1
  elif(operator == '('):
    priOp = 4
  else:
    priOp = 0
 
  if(operator2 == '^'):
    priOp2 = 3
  elif(operator2 == '*' or operator2 == '/'):
    priOp2 = 2
  elif(operator2 == '+' or operator2 == '-'):
    priOp2 = 1
  elif(operator2 == '('):
    priOp2 = 0
  else:
    priOp2 = 0
 
  return (priOp > priOp2)


n = int(input())

opStack = []
for i in range(n):
  answer = ''
  expression = input()
  for j in range (len(expression)):
    if (expression[j].isalpha()):
      answer += expression[j]
    elif(expression[j] == '('):
      opStack.append(expression[j])
    elif(expression[j] == ')'):
      op = opStack.pop()
      while (op != '(' and op != ''):
        answer += op
        try:
          op = opStack.pop()
        except IndexError:
          op = ''
    else:
      while (True):
        try:
          op = opStack.pop()
        except IndexError:
          op = ''
        if (defPriority(expression[j], op)):
          opStack.append(op)
          opStack.append(expression[j])
          break
        else:
          answer += op
          
  for j in range(len(opStack)):
    op = opStack.pop()
    if (op == '(' or op == ')'):
      break
    else:
      answer += op

  print(answer)