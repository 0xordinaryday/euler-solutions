import math

def isPal(num):
    numStr = str(num)
    return numStr == numStr[::-1]

'''    
def sumSquares(num, start):
    maximum = int(math.sqrt(num))+1
    total = 0
    if start == maximum:
        return False
    else: 
        for i in range(start,maximum):
            total += i**2
            if total == num:
                return True
            elif total > maximum:
                return sumSquares(num, start+1)
                
    
result = 0    
for i in range(2,1000):
    if isPal(i) and sumSquares(i, 1):
        print i
        result += i
        
print result        
'''
squareList = []
for i in range(1,10001):
    squareList.append(i**2)


squareSums = []
inc = 1
while inc < len(squareList):
    for idx, entry in enumerate(squareList):
        try: 
            result = entry
            for i in range(1,inc+1):
                result += squareList[idx+i]
                if result > 100000: #00
                    break
            squareSums.append(result)
        except IndexError:
            break
    inc += 1
    
print max(squareSums)
#print squareList
'''
setSums = set(squareSums)

total = 0
for entry in setSums:
    if entry < 10000000 and isPal(entry):
        total += entry
        
print total        
'''
    