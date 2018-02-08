# product = multiplicand * multiplier
# 987654322

import itertools
from datetime import datetime
startTime = datetime.now()


products = []
perm = list("".join(string) for string in itertools.permutations('123456789'))
for entry in perm:
    for xpos in range(2,5):
        for eqpos in range(xpos+1,xpos+3):
            if int(entry[:xpos])*int(entry[xpos:eqpos]) == int(entry[eqpos:]):
                products.append(entry[eqpos:])
                
results = set(products) # get rid of duplicates
result = 0
for entry in results:
    result += int(entry)
    
print result
print datetime.now() - startTime             

#gives the correct answer of 45228 in 4.4 seconds   
