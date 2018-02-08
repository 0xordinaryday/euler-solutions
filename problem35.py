"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def doRotations(numString): # number as a string
    digitList = []
    rotList = []
    for digit in numString:
        digitList.append(digit)
    for rotation in range(len(numString)):
        digitList.append(digitList.pop(0)) # rotates the digits by one
        rotList.append(''.join(digitList)) # makes the list into a string and appends it
    return rotList
    
with open('prime_list.txt', 'r') as f:
    lines = f.readlines()
    
    
count = 0    
lines = [n.strip('\n') for n in lines]

def checkRotations(rotations):
    for rotation in rotations:
        if rotation not in lines:
            return False
    return True


for number in lines:
    rotations = doRotations(number)
    if checkRotations(rotations):
        count += 1
        #print number
print count - 1

# Answer is 55. This solution gives 56 but they don't count 1 as a prime, hence -1.