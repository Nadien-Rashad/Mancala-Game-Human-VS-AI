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

