"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

sum = 0

def decimalIsPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else: return False
    
def binaryIsPalindrome(number):
    if str(bin(number)[2:]) == str(bin(number)[2:])[::-1]:
        return True
    else: return False
    
for i in range(1000000):
    if decimalIsPalindrome(i) and binaryIsPalindrome(i):
        sum += i
        
print sum

# answer is 872187 which is correct