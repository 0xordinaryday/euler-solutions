"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

#list amicable

amicableList = [] # to hold amicable numbers


#startNumber = 220
for number in range(1, 10001):
    listAmicable = []
    for i in range(1, number):
        if number % i == 0:
            listAmicable.append(i)
        
    testAmicable = sum(listAmicable)
    listTest = []
    for i in range(1, testAmicable):
        if testAmicable % i == 0:
            listTest.append(i)
        
    if sum(listTest) == number and number != testAmicable:
        amicableList.append(number)
    
print sum(amicableList)

# answer is 31626 which is correct