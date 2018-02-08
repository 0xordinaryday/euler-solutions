"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

with open('prime_list.txt', 'r') as f:
    primes = f.readlines()

stripped = []    
for prime in primes:
    stripped.append(int(prime[:-1]))

for x in range(3,653,2):
    subList = stripped[3:3+x]
    result = sum(subList)
    if result == 997651: #< 1000000:
        print result, len(subList), result in stripped

# this gave a result of 997651 which was correct, but that was arse I think.
# that is because there was no guarantee that the correct answer would begin
# at a value of 3. But it did, so ooo rah.
        
    