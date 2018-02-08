"""generate primes and write to file, up to 1,000,000"""

import math

def isPrime(number):
    assert type(number) == int
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

with open('prime_list.txt', 'w') as outfile:    
    for i in range(1, 1000000):
        if isPrime(i):
            strWrite = str(i) + '\n'
            outfile.write(strWrite)
        
        