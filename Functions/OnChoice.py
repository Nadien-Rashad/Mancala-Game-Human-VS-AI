def OnChoice(choice, choiceID): 
    """
    The function that applies all the game rules.
    Parameters : choice is the value in the pocket, 
                 choiceID is the index of this pocket.

    """

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
