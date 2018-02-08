"""fib to 1000 digits"""


fibs = []
next = 0
first = 1
second = 1
pos = 2
while len(str(next)) < 1000:
    next = first + second
    first = second
    second = next
    pos += 1
    
print pos # don't actually append to list
#answer is 4782, which is correct
