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
    
