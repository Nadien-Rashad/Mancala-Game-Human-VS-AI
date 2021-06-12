import numpy as np

pits = [4,4,4,4,4,4,4,4,4,4,4,4]
store = [0,0]
choiceIDs = [0,1,2,3,4,5,6,7,8]
stealing=0
maxTreeDepth = 5
plays = True

def DrawBoard(binAmount,store):
    """
    binAmount: An array of 12 values has the amount of stones in  every pocket 
    store: An array of two values of the players’ scores 
    Used to present the Mancala board from the start of the game and after each play.

    """

    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ str(binAmount[5])+"  | "+ str(binAmount[4])+"  | "+ str(binAmount[3])+"  | "+ str(binAmount[2])+"  | "+ str(binAmount[1])+"  | "+ str(binAmount[0])+"  |    |")
    print("| "+ str(store[0]) +"  |----+----+----+----+----+----| "+ str(store[1])+"  |")
    print("|    | "+ str(binAmount[6])+"  | "+ str(binAmount[7])+"  | "+ str(binAmount[8])+"  | "+ str(binAmount[9])+"  | "+ str(binAmount[10])+"  | "+ str(binAmount[11])+"  |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("       H    I    J   K     L     M")

def checkIfEnd(pits):
    
    counter = 0
    for i in range(0,6):
        if (pits[i] != 0):
            break
        else:
            counter = counter + 1
    # game is over
    if (counter == 6):
        for i in range(6, 12):
            store[1]  = store[1]  + pits[i] 
        for i in range(0,12):
            pits[i]=0
        return True
    else:
        counter = 0
        for i in range(6,12):
            if (pits[i]  != 0):
                break
            else:
                counter = counter + 1
        # game if over
        if (counter == 6):
            for i in range(0, 6):
                store[0]  = store[0]  + pits[i] 
            for i in range(0,12):
                pits[i]=0
            return True
    return False

def Add_pit(value):
    """
    add the value by one when it’s called 
    Returns the value to be stored in the pocket or the store
    """
    temp_value = value
    bin = temp_value+1
    return bin

def checkEmptyField(choice, choiceIndex):
  
    global stealing
    temp_value = choice 
    oppositeFieldIndex = 11 - choiceIndex 
    temp_opposite_value = pits[oppositeFieldIndex] #value of stones in the opposite
    if (temp_value == 0 and temp_opposite_value != 0 and stealing==1):
        for  i in range(0,  temp_opposite_value +1 ):
            store[whoseTurn]=Add_pit(store[whoseTurn])
        pits[oppositeFieldIndex]=0
        print("stealing occureed")
    else:
        pits[choiceIndex]=Add_pit(choice)

def OnChoice(choice, choiceID): 
    

    global whoseTurn, play
    value = choice 
    pits[choiceID]=0 
    startingIndex = choiceID+1 
    i = choiceID+1   
    while (i < choiceID+value+1):  
        # check if the points need to be inserted into left base
        if(startingIndex == 6 and whoseTurn == 0):
            store[whoseTurn]=Add_pit(store[whoseTurn])
            
            # check if the point inserted into the store was the last pit.
            # if so, give the same  player another turn (else instruction)
            if (i+1 < choiceID+value+1): 
               pits[startingIndex]= Add_pit(pits[startingIndex])
            else:
                whoseTurn = -1 * whoseTurn + 1
            startingIndex = startingIndex + 1
            i = i + 2
         
        elif(startingIndex == 12 and whoseTurn == 1):
            store[whoseTurn]=Add_pit(store[whoseTurn])
            # check if the point inserted into the store was the last pit.
            # if so, give the same  player another turn (else instruction)
            if (i+1 < choiceID+value+1):
                pits[0]=Add_pit(pits[0])
            else:
                whoseTurn = -1 * whoseTurn + 1
            i = i+2
            startingIndex = 1
        # reset counting at the right side
        elif(startingIndex == 12):
            startingIndex = 0

            
        # check for stealing
        else:   
            if( i+1 == choiceID+value+1 and (startingIndex < 6 and whoseTurn == 1 or startingIndex > 5 and whoseTurn == 0)):
                    checkEmptyField(pits[startingIndex], startingIndex)

        # increase the field value normally
            else:
                pits[startingIndex]=Add_pit(pits[startingIndex]) 
            startingIndex = startingIndex + 1         
            i = i+1   

    whoseTurn = -1 * whoseTurn + 1
    
    bool=checkIfEnd(pits)
    if(bool==True):
      
        if (store[1] > store[0]):
            
            print("*******  You WINS :D *******")
            print("Score of the WINNER:", store[1])
        elif (store[1] < store[0]):
            
            print("*******  The AI WINS  *******")
            print("Score of the WINNER:", store[0])
        
                
    return pits,store

def GetState(pits, store, whoseTurn):
    pit_fields_temp = []
    pit_fields = []
    for i in range(0, 14):
        if i < 6:
            pit_fields_temp.append(pits[i])
        elif i == 6:
            pit_fields_temp.append(store[0])
        elif i < 13:
            pit_fields_temp.append(pits[i-1])
        elif i == 13:
            pit_fields_temp.append(store[1])
    if(whoseTurn == 1):
        for i in range(7,14):
            pit_fields.append(pit_fields_temp[i])
        for i in range(0,7):
            pit_fields.append(pit_fields_temp[i])
    else:
        pit_fields = pit_fields_temp       
    return pit_fields

def play(pit_fields, choice):
    whoseTurn = 0
    if choice > 5: # law el choice akbar men 5 yeb2a da el player el tany
        whoseTurn = 1

    MyIndex = choice + 1
    i = choice + 1
    value = pit_fields[choice]
    pit_fields[choice] = 0

    while(i < choice+1+value): #ana bazwed el amaken el sah w msh bazwed el bucket bta3 el player el tany
        if(whoseTurn == 0 and MyIndex != 13):
            pit_fields[MyIndex] += 1
        elif(whoseTurn == 1 and MyIndex != 6):
            pit_fields[MyIndex] += 1
        else: 
            if(whoseTurn == 0): # player 1 hayl3ab f hazwed 1 3ala kool element fel list bta3to men ba3d elly ekhtarha
                MyIndex = 0
                pit_fields[MyIndex] += 1
            else:
                MyIndex += 1
                pit_fields[MyIndex] += 1
        i += 1
        MyIndex += 1

        HisIndex = 13 - MyIndex
        # 3ashan at2aked eza kan fe door tany hatl3b f b check 3ala akher wahda etla3bet 
        if(i == choice+1+value and ((whoseTurn == 0 and MyIndex-1 == 6) or (whoseTurn == 1 and MyIndex-1 == 13))):
            continue
        # hena nat2aked en law fe stealing yetle3eb f bat2ked eno el makan elly odam el field el fady msh fady
        elif(i == choice+1+value and pit_fields[HisIndex] != 0 and pit_fields[MyIndex-1]-1 == 0 and((whoseTurn == 0 and MyIndex-1 < 6) or (whoseTurn == 1 and MyIndex-1 > 6 and MyIndex-1 < 13))):
            if(whoseTurn == 0):
                pit_fields[6] += pit_fields[HisIndex] + 1
                pit_fields[MyIndex-1] = 0
                pit_fields[HisIndex] = 0
            else :
                pit_fields[13] += pit_fields[HisIndex] + 1
                pit_fields[MyIndex-1] = 0
                pit_fields[HisIndex] = 0
            whoseTurn = -1 * whoseTurn + 1
        elif(i == choice+1+value):
            whoseTurn = -1 * whoseTurn + 1

        if(MyIndex == 14):
            MyIndex = 0

        # Evaluating Results
        if(pit_fields[0] == 0 and pit_fields[1] == 0 and pit_fields[2] == 0 and pit_fields[3] == 0 and pit_fields[4] == 0 and pit_fields[5] == 0):
            pit_fields[13] = pit_fields[13] + pit_fields[7] + pit_fields[8] + pit_fields[9] + pit_fields[10] + pit_fields[11] + pit_fields[12]
            for i in range(7, 13):
                pit_fields[i] = 0
            break
            
        elif(pit_fields[7] == 0 and pit_fields[8] == 0 and pit_fields[9] == 0 and pit_fields[10] == 0 and pit_fields[11] == 0 and pit_fields[12] == 0):
            pit_fields[6] = pit_fields[6] + pit_fields[0] + pit_fields[1] + pit_fields[2] + pit_fields[3] + pit_fields[4] + pit_fields[5]
            for i in range(0, 6):
                pit_fields[i] = 0
            break
            
    return pit_fields, whoseTurn
    

def checkGameEnd(pit_fields):
    playerOne = True
    playerTwo = True

    for i in range(0, 6):
        if pit_fields[i] > 0:
            playerOne = False
    if (playerOne):
        return 1

    for i in range(7, 13):
        if pit_fields[i] > 0:
            playerTwo = False
    if (playerTwo):
        return 2

    return 0

def GetBestMove(pit_fields, whoseTurn, searchtreeDepth, no_AnalyzedStates, alpha, beta):
    v = 0
    noOfAvailableMoves = 6
    no_AnalyzedStates[0] += 1
    ActionScore = []
    START = 0
    END = 6
    temp_pit_fields = pit_fields[:]
    whoseTurnAtCurrentDepth = whoseTurn

    if (whoseTurn == 1):
        START = 7
        END = 13
        v = beta
    else :
        v = alpha

    gameEnd = checkGameEnd(temp_pit_fields)
    if(searchtreeDepth ==   maxTreeDepth or gameEnd != 0): 
        if (gameEnd == 1):
            return temp_pit_fields[6] - temp_pit_fields[13] + sum(temp_pit_fields[7:12])
        elif (gameEnd == 2):
            return temp_pit_fields[6] - temp_pit_fields[13] - sum(temp_pit_fields[0:5])
        else:
            return temp_pit_fields[6] - temp_pit_fields[13]
    else:
        #bagarab kool el possible moves
        for i in range(START, END):
            temp_pit_fields = pit_fields[:]

            # 3ayza a3raf hayhsal cuttoff wala la2 f b check law alpha akbar men beta fel two turns
            if(whoseTurnAtCurrentDepth == 0 and v > beta):
                break
            elif whoseTurnAtCurrentDepth == 1 and v < alpha :
                break

            if(temp_pit_fields[i] == 0):
                ActionScore.append(temp_pit_fields[6] - temp_pit_fields[13])
                continue
            else:
                # byhseb el state nateget el move
                temp_pit_fields, whoseTurn =   play(temp_pit_fields, i)
                
                # call the function recursively (advance in depth - DFS) 3ashan yebny el tree 3ala asa el depth elli ana medeyaholo 
                ActionScore.append(GetBestMove(temp_pit_fields, whoseTurn, searchtreeDepth+1, no_AnalyzedStates, alpha, beta))

                # update alpha and beta values
                if(whoseTurnAtCurrentDepth == 0) :
                    if( ActionScore[-1] > v):
                        v = ActionScore[-1]
                    alpha = max(ActionScore)
                elif (whoseTurnAtCurrentDepth == 1):
                    if (ActionScore[-1] < v):
                        v = ActionScore[-1]
                    beta = min(ActionScore)
                
    if searchtreeDepth == 0:
        ActionScore = np.asarray(ActionScore)
        maxScore = np.random.choice(np.flatnonzero(ActionScore == ActionScore.max()))
        while(pit_fields[maxScore] == 0):
            # hena ana b avoid law el choice bta3o b zero 
            ActionScore[maxScore] = -100
            maxScore = np.random.choice(np.flatnonzero(ActionScore == ActionScore.max()))
        return maxScore

    # return score in case of a max node
    if(whoseTurnAtCurrentDepth == 0):
        if not ActionScore:
            return 50
        else:
            return max(ActionScore)

    # return score in case of a min node
    if(whoseTurnAtCurrentDepth == 1):
        if not ActionScore:
            return -50
        else:
            return min(ActionScore)

def makeDecision(pits, store, whoseTurn):
    searchtreeDepth = 0
    # extract an array of fields from the current state
    pit_fields =   GetState(pits, store, whoseTurn)
    whoseTurn = 0
    
    # analyzed states counter
    no_AnalyzedStates = []
    no_AnalyzedStates.append(0)
    #print(no_AnalyzedStates)
    #  pruning
    alpha = -50
    beta = 50
    
    # call the function finding the most optimal move
    choice =   GetBestMove(pit_fields, whoseTurn, searchtreeDepth, no_AnalyzedStates, alpha, beta)
    #print("Number of Analyzed states: ", no_AnalyzedStates)
    return choice


#****************************************************************************************#
print("")
print(" ************************************* ")
print(" *    WELCOME to MANCALA GAME :D     * ")
print(" ************************************* ")
stealing=int(input("With stealing mode or not,  Enter 1 for yes & 0 for No "))
whoseTurn=int(input("Do you want to start playing: Enter 1 for YES & 0 for NO " ))
Difficulty_level=int(input("Choose the difficulty Level "))
if(Difficulty_level==1 | Difficulty_level==2):

    maxTreeDepth = 3
elif(Difficulty_level==3 | Difficulty_level==4):

    maxTreeDepth = 5
elif(Difficulty_level==5 | Difficulty_level==6|Difficulty_level==6):
    
    maxTreeDepth = 7
else:
     maxTreeDepth = 10



DrawBoard(pits,store)

while(plays):

     if (whoseTurn == 0):   
        print("AI turn ...")
        
        #***For Ai***
        choice=makeDecision(pits, store, whoseTurn)
        
        print("choice is" ,choice)
            
        pits,store = OnChoice(pits[choice], choice)
    
        DrawBoard(pits,store)
        bool=checkIfEnd(pits)
        if(bool==True): break
     
     elif (whoseTurn==1):
        print("Player's BB turn ...")

        choiceSTR = str.capitalize(input("Please Enter Your chosen bin from H to M -> "))
       
    
        if   (choiceSTR == "H") : choice =6
        elif (choiceSTR == "I") : choice =7
        elif (choiceSTR == "J") : choice =8
        elif (choiceSTR == "K") : choice =9
        elif (choiceSTR == "L") : choice =10
        elif (choiceSTR == "M") : choice =11
        else:
            (print("Invalid Choice"))
            choiceSTR = str.capitalize( input("Please Enter valid bin from H to M -> "))
            if   (choiceSTR == "H") : choice =6
            elif (choiceSTR == "I") : choice =7
            elif (choiceSTR == "J") : choice =8
            elif (choiceSTR == "K") : choice =9
            elif (choiceSTR == "L") : choice =10
            elif (choiceSTR == "M") : choice =11
      
        
        
        pits ,store = OnChoice(pits[choice], choice)
        DrawBoard(pits,store)
        #print("base array",store)
        bool=checkIfEnd(pits)
        if(bool==True): break
     
   
     
