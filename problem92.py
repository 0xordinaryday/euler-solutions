"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 - 32 - 13 - 10 - 1 - 1
85 - 89 - 145 - 42 - 20 - 4 - 16 - 37 - 58 - 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

count = 0
myList = []

def calcChain1(number):
    """ number is an int"""
    if number == 1:
        return True
    elif number == 89:
        return False
    else: 
        numStr = str(number)
        sum = 0
        for digit in numStr:
            sum += int(digit)**2
        return calcChain1(sum)
        
def calcChain2(number, myList):
    """ number is an int"""
    numStr = str(number)
    sum = 0
    for digit in numStr:
        sum += int(digit)**2
    if sum in myList: return True
    else: return False

for i in range(1,700):
    if calcChain1(i): # if led to 1
        count += 1
        myList.append(i)
        
for i in range(700,10000000):
    if calcChain2(i, myList):
        count += 1
    
print count, 9999999 - count

# answer is 8581146 which is correct but a bit slow