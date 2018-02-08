"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def calcFactorial(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    return factorial
    
def calcSum(value):
    sum = 0
    for digit in str(value):
        result = calcFactorial(int(digit))
        sum += result
        #print sum
    return sum

#print calcSum(145)
    
total = 0
for i in range(3, 2000000):
    if i == calcSum(i):
        total += i
        
print total

# answer is 40730 - there are only two of these numbers!

        
    
 
    
    