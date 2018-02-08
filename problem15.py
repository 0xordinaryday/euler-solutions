# path counting in Python
'''
def numPaths(x,y):
    if x == 1 or y == 1:
        return 1
    else:
        return numPaths(x-1, y) + numPaths(x, y-1)
        
print numPaths(15,15)        
'''

# path counting in Racket
'''
(define (numPaths x y)
  (cond [(or (= x 1) (= y 1)) 1]
        [else (+ (numPaths(- x 1) y) (numPaths x (- y 1)))]))
'''        

# actual formula is (2n)!/n!**2
import math
print math.factorial(20*2)/math.factorial(20)**2
# gives answer of 137846528820, which is correct