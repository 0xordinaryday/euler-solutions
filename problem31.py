from decimal import *

mystr = str(Decimal(1)/Decimal(7))
print mystr
mystr2 = str(Decimal(1)/Decimal(29))
print mystr2

def repeats(inputStr):
    if len(inputStr) < 30:
        return False
    else: return True
    
#def repLength(inputStr):
    
    