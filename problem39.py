from collections import Counter
from datetime import datetime
startTime = datetime.now()

squareList = []
for i in range(2,500,2): # perimeter must be even, max length for c is perimeter/2 (so use 500)
    squareList.append(i**2)
    
#print squareList    

resultList = []
for a in squareList:
    for b in squareList:
        if b > a:
            break
        else:
            c = a + b
            if c in squareList:
                resultList.append((a,b,c))
    
perimList = []    
for abc in resultList:
    perimeter = int((abc[0]**0.5)+(abc[1]**0.5)+(abc[2]**0.5))
    if perimeter <= 1000:
        perimList.append(perimeter)
    
data = Counter(perimList)
print data.most_common(1)
print datetime.now() - startTime

# gives 840, which is correct, in about 0.1 seconds.