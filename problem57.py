"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

root 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

# 1, 3, 7, 17, 41, 99, 239, 577
# multiply by two and add previous term

# 1, 2, 5, 12, 29, 70, 169, 408, 985
# same, double and add previous

lastNumerator = 1
lastDenominator = 1
numerator = 3
denominator = 2

countCondition = 0

for i in range(1000):
    nextNumerator = numerator*2 + lastNumerator
    nextDenominator = denominator*2 + lastDenominator
    if len(str(nextNumerator)) > len(str(nextDenominator)):
        countCondition += 1
    lastDenominator = denominator
    lastNumerator = numerator
    denominator = nextDenominator
    numerator = nextNumerator
    #print str(numerator) + '/' + str(denominator)
    
print countCondition

# answer is 153 which is correct. Quite fast.