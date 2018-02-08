""" If the numbers 1 to 5 are written out in words: one, two, three, four, 
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used?
    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
    contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
    "and" when writing out numbers is in compliance with British usage.
"""

"""one two three four five six seven eight nine ten
    eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
    thirty forty fifty sixty seventy eighty ninety hundred thousand"""
    
listOfNumbers = []
digits = ['one','two','three','four','five','six','seven','eight','nine','ten']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']
for i in range(len(digits)):
    listOfNumbers.append(digits[i])
for i in range(len(teens)):
    listOfNumbers.append(teens[i])
for i in range(0,8):
    listOfNumbers.append(tens[i])
    for j in range(len(digits) - 1):
        listOfNumbers.append(tens[i] + ' ' + digits[j])
        
# list now contains up to 99
for i in range(len(digits) - 1):
    tempString = (digits[i] + ' hundred')
    listOfNumbers.append(tempString)
    for j in range(99):
        listOfNumbers.append(tempString + ' and ' + listOfNumbers[j])
        
listOfNumbers.append('one thousand')
    
#print len(listOfNumbers)

#count items now
count = 0
itemlen = 0
letters = 'abcdefghijklmnopqrstuvwxyz'
for item in listOfNumbers:
    itemlen = 0
    for letter in item:
        if letter in letters:
            itemlen += 1
    count += itemlen
    
print count
# answer is 21124, which is correct