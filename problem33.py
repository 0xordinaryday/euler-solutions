for i in range(10,100):
    numerator = float(i)
    for j in range(10,100):
        fraction = numerator/j
        # print numerator, j
        if numerator != j:
            if (str(i))[1] == (str(j))[0] and float(str(j)[1]) != 0:
                reduced = float(str(i)[0])/float(str(j)[1])
                if reduced == fraction and i < j:
                    print i, j

#387296
#38729600
# this gives the above, which works out to 1/100, which is correct (100 is the answer)
