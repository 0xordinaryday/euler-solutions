''' old version
def noRepeats(num):
    numStr = str(num)
    length = len(numStr)
    if '0' in numStr:
        return False
    elif str(length + 1) in str(num):
        return False
    elif str(length + 2) in str(num):
        return False
    for i in range(length):
        if numStr[i] in numStr[(i+1):]:
            return False
    else: return True

def isPrime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    else:
        return True 

#not used
        def biggestPrime(startval):
    prime = False
    while not prime:
        n = startval
        if n % 2 == 0:
            startval -= 1
        else:
            for x in range(3, int(n**0.5 + 1), 2):
                if n % x == 0:
                    prime = False
                    startval -= 1
                    break
                else: 
                    prime = True
                    return n

starting = 87654321

def targetMet(value):
    if noRepeats(value):
        if isPrime(value):
            return True
        else: return False
    else: return False
                           
while not targetMet(starting):
    starting -= 1
    
print starting
# gives answer of 7652413 which is correct but a bit slow... could be refactored.
'''

def isPrime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    else:
        return True 

import itertools

perm = list("".join(string) for string in itertools.permutations("1234567"))
perm = list(set(perm))

primeList = []
for entry in perm:
    if str(entry[-1:]) in '13579':
        if isPrime(int(entry)):
            primeList.append(entry)
        
print max(primeList)

# also gives correct answer and is basically instant but doesn't check for 8 or 9....