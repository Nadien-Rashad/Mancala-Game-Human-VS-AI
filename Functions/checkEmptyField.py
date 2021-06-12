def checkEmptyField(choice, choiceIndex):
    """
      For stealing mode
      parameters: choice is the value in the pocket, 
                  choiceIndex is the index of this pocket.
      Checks If the last piece dropped is in an empty pocket on the player’s side,
      you capture that piece and any pieces in the pocket directly opposite.
      So this functions applies those two conditions:
      1)if last pit  dropped in an empty pocket on the player’s side
      2)This pit is captured and pieces directly opposite and added to the player’s store.

    """
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
