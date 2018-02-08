def findDivisors(n):
    count = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            count += 1
    return count+1 # for the number itself
    
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
    
countNum = 0    
for i in range(1,100000):#000):
    if not isPrime(i):
        if not isPrime(i + 1):
            if findDivisors(i) == findDivisors(i+1):
                countNum += 1
        
print countNum        
            