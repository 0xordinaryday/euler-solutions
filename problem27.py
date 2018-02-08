def isPrime(num):
    if num < 2: 
        return False
    elif num % 2 == 0:
        return False
    for i in range(3,(num/2)+1):
        if num % i == 0:
            return False
    else: return True
    
# n**2 + na + b
# b < -1000, 1000
# b must be prime

primeList = []
for i in range(1001):
    if isPrime(i):
        primeList.append(i)
        
#print len(primeList)

maxPrimes = 0
maxValue_a = 0
maxValue_b = 0

for a in range(-1000,1001):
    for b in primeList:
        countPrimes = 0
        for n in range(0,100):
            result = (n*n) + (n*a) + b
            if not isPrime(result):
                break
            else:
                #print result
                countPrimes += 1
                if countPrimes > maxPrimes:
                    maxPrimes = countPrimes
                    maxValue_a = a
                    maxValue_b = b
                        
print maxPrimes, maxValue_a, maxValue_b, maxValue_a*maxValue_b

#gives answer of -59231 which is correct                    
                
