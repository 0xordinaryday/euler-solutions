from datetime import datetime
startTime = datetime.now()

def rprime(a,b):
    while b: #b != 0
        a,b = b, a%b
    return a == 1

def coPrimeCount(num):    
    count = 0
    for i in range(num):
        if rprime(num,i):
            count += 1
    return count
    
max = 0
n = 0
testval = 30000

for i in range(20,testval,10):
    result = float(i)/coPrimeCount(i)
    if result > max:
        max = result
        n = i

print n        
print datetime.now() - startTime
  
  
Famous_Greeks - Copy.zip