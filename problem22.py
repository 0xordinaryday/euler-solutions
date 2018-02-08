"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

with open('p022_names.txt', 'r') as f:
    lines = f.read()

names = lines.split(',')
names = [n.strip('"') for n in names]
#print names[0:10]

#sort list
names.sort()

# score names
# ord('A') - 64
scoredList = []
for name in names: 
    score = 0
    for letter in name:
        score += ord(letter) - 64
    scoredList.append(score)
  
#print scoredList[0:10]
#print len(names)

finalList = []
for i in range(len(scoredList)):
    newScore = scoredList[i] * (i + 1)
    finalList.append(newScore)

#print scoredList[0:20]
#print finalList[0:20]
    
print sum(finalList)

# answer is 871198282