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
