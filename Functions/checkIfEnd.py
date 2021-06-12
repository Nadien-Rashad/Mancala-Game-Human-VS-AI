def checkIfEnd(pits):
    """
    Checks if the value of pits in all 6 pockets on one 
    side of the Mancala board is empty this means the game came to end 
    then applying rule 7 ; the pits on the other side of the game 
    is captured all and put on the player’s store.
    Returns True if the condition are checked

    """
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
