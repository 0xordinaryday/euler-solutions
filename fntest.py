def noRepeats(num):
    numStr = str(num)
    flag = True;
    for i in range(len(numStr)):
        if numStr[i] in numStr[(i+1):]:
            flag = False
    return flag
    
print noRepeats(10987651)


    
