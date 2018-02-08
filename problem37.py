def isPrime(n):
    if n == 1:
        return False
    elif len(str(n)) > 1 and str(n)[-1] in '024568':
        return False
    elif len(str(n)) == 1 and str(n)[-1] in '0468':
        return False    
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    else:
        return True 

primeList = []        
for i in range(10,1000001):
    if isPrime(i):
        primeList.append(i)
        
def isTruncatableFwd(primeStr):
    if len(primeStr) == 1 and isPrime(int(primeStr)):
        return True
    elif isPrime(int(primeStr[1:])):
        return isTruncatableFwd(primeStr[1:])
    else: return False
    
def isTruncatableRev(primeStr):
    if len(primeStr) == 1 and isPrime(int(primeStr)):
        return True
    elif isPrime(int(primeStr[:-1])):
        return isTruncatableRev(primeStr[:-1])
    else: return False    
        
truncatable = []        
for prime in primeList:
    primeStr = str(prime)
    if isTruncatableFwd(primeStr) and isTruncatableRev(primeStr):
        truncatable.append(prime)
        
print sum(truncatable)

#gives answer of 748317 which is correct