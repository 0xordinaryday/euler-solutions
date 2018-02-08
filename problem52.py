"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def meetsCondition(number):
    string = str(number)
    for i in range(2,7):
        for char in str(i*number):
            if char not in string:
                return False
    return True 
    
j = 1    
while True:
    if meetsCondition(j):
        break
    j += 1
    
print j

# answer is 142857 which is correct, and it was also pretty fast!