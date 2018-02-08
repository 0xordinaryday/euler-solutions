import itertools

def isPrime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    else:
        return True 

primeList = []
for i in range(1001,10000,2):
    if isPrime(i):
        primeList.append(str(i)) # primeList are strings
        
candidates = []    
for entry in primeList:
    perm = list("".join(string) for string in itertools.permutations(entry))
    perm.remove(entry)
    count = 0
    for item in perm:
        if item in primeList and item != entry:
            count += 1
    if count > 3:
        candidates.append(int(entry))

def isPerm(number, totest):
    numStr = str(number)
    perm = list("".join(string) for string in itertools.permutations(numStr))
    perm.remove(numStr)
    if str(totest) in perm:
        return True
    else: return False
        
for i in range(len(candidates) -1):
    for offset in range(1,int(len(candidates)/3)):
        #print candidates[i], candidates[i+offset], candidates[i+offset]-candidates[i]
        upperbound = i + offset
        if upperbound >= len(candidates):
            upperbound = len(candidates) - 1
        difference = (candidates[upperbound]-candidates[i])
        if (candidates[i] + (2*difference)) in candidates and isPerm(candidates[i], candidates[i]+difference) and isPerm(candidates[i], candidates[i]+2*difference):
            print candidates[i], candidates[i]+difference, candidates[i]+2*difference
            
#gives answer of 296962999629, which is correct. Fairly quick but ugly.