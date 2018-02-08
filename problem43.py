def noRepeats(num):
    numStr = str(num)
    length = len(numStr)
    for i in range(length):
        if numStr[i] in numStr[(i+1):]:
            return False
    return True

def genList(input_num):
    outlist = []
    for i in range(1,1000):
        if (i % input_num == 0) and noRepeats(i):
            if i < 10:
                out = '00' + str(i)
            elif i < 100:
                out = '0' + str(i)
            else:
                out = str(i)
            outlist.append(out)
    return outlist
    
list2 = genList(2)
list3 = genList(3)  
list5 = genList(5)  
list7 = genList(7)  
list11 = genList(11)  
list13 = genList(13)
list17 = genList(17)    

worklist = []
templist = []

for x in list17:
    for y in list13:
        if x[:2] == y[1:]:
            worklist.append(y[0]+x)
            
for x in worklist:
    for y in list11:
        if x[:2] == y[1:]:
            templist.append(y[0]+x)
            
worklist = []
for x in templist:
    for y in list7:
        if x[:2] == y[1:]:
            worklist.append(y[0]+x)
            
templist = []
for x in worklist:
    for y in list5:
        if x[:2] == y[1:]:
            templist.append(y[0]+x)   

worklist = []
for x in templist:
    for y in list3:
        if x[:2] == y[1:]:
            worklist.append(y[0]+x)
            
templist = []
for x in worklist:
    for y in list2:
        if x[:2] == y[1:]:
            templist.append(y[0]+x)              
            
numlist = []
for i in templist:
    if noRepeats(int(i)) and (int(i) > 99999999):
        numlist.append(i)
        
numbers = '123456789'

finalList = []
for entry in numlist:
    for num in numbers:
        if num not in entry:
            finalList.append(num+entry)
        
#print finalList
sum = 0
for entry in finalList:
    sum += int(entry)
    
print sum
# answer given is 16695334890, which is correct, woo hoo.
