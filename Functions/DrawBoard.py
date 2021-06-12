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
