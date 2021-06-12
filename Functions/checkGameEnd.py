
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
