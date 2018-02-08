#size 1001 * 1001
# halfway is 500

from datetime import datetime
startTime = datetime.now()

size = 1001

# create a sequence of moves, of form x+, y+, x-, x-, y-, y-, etc
# sequence goes plus x, plus y, minus x, minus y then repeats
# sequence increases from 1x 1y, 2x 2y, 3x 3y etc
sequence = []
inc = '-'
for i in range(1,1100):
    if inc == '+':
        inc = '-'
    else: inc = '+'
    for j in range(i):
        sequence.append('x'+inc)
    for j in range(i):
        sequence.append('y'+inc)

# sequence list is longer than needed, so trim it back        
final_seq = sequence[:(size**2)]

# make big empty (zero filled) list of lists
emptyRow = []
for i in range(size):
    emptyRow.append(0)
    
myArray = []
for i in range(size):
    myArray.append(emptyRow[:])
    
# get halfway point
x = size/2
y = size/2

# fill 'array' with values
for i in range(1,((size)**2)+1):
    try:
        myArray[x][y] = i
        move = final_seq[i-1]
        
        if move == 'x+':
            x += 1
        elif move == 'x-':
            x -= 1
        elif move == 'y+':
            y += 1
        else:
            y -= 1 
    except IndexError: # when we fill the whole thing
        break

# sum the diagonals        
result = 0
for i in range(size):
    result += myArray[i][i]
    
for j in range(size):
    result += myArray[j][size-j-1]
    
print result-1 # don't double count the centre value (which is 1)

print datetime.now() - startTime

# gives the correct answer of 669171001 in 0.57 seconds


        
