import itertools

perm = list("".join(string) for string in itertools.permutations("0123456789"))

perm.sort()

print perm[999999]

#gives answer of 2783915460, which is correct
        