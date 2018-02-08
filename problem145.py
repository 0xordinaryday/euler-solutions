def reversible(n):
    # assume at least 2 digits
    if str(n)[-1] == '0':
        return False
    elif str(n)[0] in '2468' and str(n)[-1] in '02468':
        return False # even plus even = even
    elif str(n)[0] in '13579' and str(n)[-1] in '13579':
        return False # odd plus odd = even
    elif containsEven(n + int(str(n)[::-1])):
        return False
    else: return True
        
def containsEven(n):
    numStr = str(n)
    if '0' in numStr or '2' in numStr or '4' in numStr or '6' in numStr or '8' in numStr:
        return True
    else: return False
    
count = 0    
for i in range(10,1000000000):
    if reversible(i):
        count += 1
              
print count