"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

bestResult = 0

for i in range(1, 100):
    for j in range(80,100): # no need to test small powers
        number = i**j
        total = 0
        for digit in str(number):
            total += int(digit)
            
        if total > bestResult:
            bestResult = total
        
print bestResult

# answer is 972, which is correct