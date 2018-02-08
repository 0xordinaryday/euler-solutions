"""
The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

#read file to list of words
with open('p042_words.txt', 'r') as f:
    lines = f.read()

words = lines.split(',')
words = [w.strip('"') for w in words]
#print words[0:10]

# make list of triangle numbers
triList = []
for x in range(1,1000):
    triList.append(int(0.5*x*(x+1)))
#print triList[0:10]

# get word values 
scoredList = []
for word in words: 
    score = 0
    for letter in word:
        score += ord(letter) - 64
    scoredList.append(score)
#print scoredList[0:10]

#count occurances of triangle words
count = 0
for score in scoredList:
    if score in triList:
        count += 1
        
print count

#answer is 162 which is correct