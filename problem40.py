"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000"""

longstr = ''
mynum = 1
while len(longstr) < 1000001:
    longstr = longstr + str(mynum)
    mynum += 1
    
res = int(longstr[0]) * int(longstr[9]) * int(longstr[99]) * int(longstr[999]) * int(longstr[9999]) * int(longstr[99999]) * int(longstr[999999])
print res

#answer is 210 which is correct, almost instant speed