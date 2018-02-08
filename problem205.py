"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""
# Peter has probability for any individual roll of 1/4**9 (262144)
# Colin has probability for any individual roll of 1/6**6 (46656)

# lets try a stochastic solution

import random

def colinRoll(colinList):
    total = 0
    for i in range(6):
        choice = random.choice(colinList)
        total += choice
    return total


def peterRoll(peterList):    
    total = 0
    for i in range(9):
        choice = random.choice(peterList)
        total += choice
    return total
    
cL = [1,2,3,4,5,6]
pL = [1,2,3,4]

cTotal = 0
pTotal = 0

colinResults = []
peterResults = []

for j in range(5000):
    cTotal = 0
    pTotal = 0
    for i in range(500):
        cTotal += colinRoll(cL)
        pTotal += peterRoll(pL)
    colinResults.append(cTotal)
    peterResults.append(pTotal)
    
print sum(colinResults)/5000.0, sum(peterResults)/5000.0, (sum(colinResults)/5000.0)/(sum(peterResults)/5000)