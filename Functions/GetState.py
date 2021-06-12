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
