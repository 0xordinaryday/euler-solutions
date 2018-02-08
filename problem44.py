#generate pentagonal numbers

pentList = []
for i in range(1,10000):
    result = i*(3*i-1)/2
    pentList.append(result)
    
def isPent(input):
    output = (1 + (1+(24*input))**0.5)/6
    if output % 1 == 0:
        return True
    else: return False
    
for i in pentList:
    for j in pentList:
        if j - i > 0:
            if isPent(i+j) and isPent(j-i):
                print i,j
            
#gives 1560090 7042750, and the difference of these is the correct answer