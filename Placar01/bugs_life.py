import numpy as np

scenarios = input() # reading the number of scenarios

for scenariosIndex in range (int(scenarios)):
        
    bugs = input().split(" ")

    bugsQuantity = int(bugs[0])
    bugsInteractions = int(bugs[1])

    controlArray = np.zeros(bugsQuantity + 1, dtype=int)
    
    suspiciousBug = False

    for i in range(bugsInteractions):
        relation = input().split(" ")
        bugA = int(relation[0])
        bugB = int(relation[1])
        
        print(controlArray)

        # bugA and bugB without sex
        if (controlArray[bugA] == 0) and (controlArray[bugB] == 0):
            controlArray[bugA] = 1  # 1 for male
            controlArray[bugB] = 2  # 2 for female
        else:
            if((controlArray[bugA] != 0) and (controlArray[bugB] != 0)):
                if(controlArray[bugA] == controlArray[bugB]):
                    suspiciousBug = True
                else:
                    suspiciousBug = False

            if (controlArray[bugA] == 0):   # bugA has no sex
                if (controlArray[bugB] == 1):
                    controlArray[bugA] = 2
                else:
                    controlArray[bugA] = 1
            else:                           # bugB has no sex
                if (controlArray[bugA] == 1):
                    controlArray[bugB] = 2
                else:
                    controlArray[bugB] = 1


    if suspiciousBug:
        print("Scenario #" + str(scenariosIndex+1) + ":")
        print("Suspicious bugs found!")
    else:    
        print("Scenario #" + str(scenariosIndex+1) + ":")
        print("No suspicious bugs found!")