def noRepeats(num):
    numStr = str(num)
    length = len(numStr)
    for i in range(length):
        if numStr[i] in numStr[(i+1):]:
            return False
    return True

numlist = [1,2,3,4,5,6,7,8,9]
maxpan = 123456789

#startval = 9

def genResults(startval):
    i = 0
    result = ''
    while len(result) < 9:
        result += str(startval*numlist[i])
        i += 1
    return result
    
for i in range(99999):
    result = int(genResults(i))
    if noRepeats(result) and (len(str(result)) == 9) and '0' not in str(result):
        if result > maxpan:
            maxpan = result
        
print maxpan
#gives result of 932718654, which is correct