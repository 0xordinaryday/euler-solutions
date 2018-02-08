#import numpy

with open('problem11.txt', 'r') as f:
    lines = f.read()
    
nonew = lines.rstrip()
words = nonew.split(',')
numlist = []
for word in words:
    numlist.append(int(word))
#print numlist

listOfL = []
for i in range(20):
    sublist = []
    for j in range(20):
        sublist.append(numlist.pop(0))
    listOfL.append(sublist)

max_prod = 0
#horizontal products
for i in range(20):
    for j in range(17):
        prod = listOfL[i][j]*listOfL[i][j+1]*listOfL[i][j+2]*listOfL[i][j+3]
        if prod > max_prod:
            max_prod = prod
print max_prod            

#vertical products
for i in range(17):
    for j in range(20):
        prod = listOfL[i][j]*listOfL[i+1][j]*listOfL[i+2][j]*listOfL[i+3][j]
        if prod > max_prod:
            max_prod = prod
print max_prod            

#NW-SE products            
for i in range(17):
    for j in range(17):
        prod = listOfL[i][j]*listOfL[i+1][j+1]*listOfL[i+2][j+2]*listOfL[i+3][j+3]
        if prod > max_prod:
            max_prod = prod 
print max_prod            

#NE-SW products            
for i in range(3,20):
    for j in range(17):
        prod = listOfL[i][j]*listOfL[i-1][j+1]*listOfL[i-2][j+2]*listOfL[i-3][j+3]
        if prod > max_prod:
            max_prod = prod 
print max_prod     

#answer is 70600674, which is correct, given in NE-SW (of course)