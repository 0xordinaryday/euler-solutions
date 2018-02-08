"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

def isabundant(num):
    divisors = []
    for i in range(1,(num/2)+1):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) > num:
        return True
    else: return False
    
abundantList = []    
for i in range(2,28124):
    if isabundant(i):
        abundantList.append(i)
        
nonAbundant = []
for i in range(1,100):
    nonAbundant.append(i)
for i in range(101,28124,2):
    nonAbundant.append(i)    

for j in range(len(abundantList)):    
    for i in range(len(abundantList) -j):
        result = abundantList[i] + abundantList[i+j]
        if result > 28124:
            break
        elif result in nonAbundant:
            nonAbundant.remove(result)
    print 'iteration', j, len(nonAbundant)
    
print sum(nonAbundant)    
#print nonAbundant

#gives the correct answer, 4179871, but takes too long to do it (5 mins?)
        
