# Description #
# In this kata you have to create all permutations of an input string and remove duplicates, if present. 
# This means, you have to shuffle all letters from the input in all possible orders


def permutations(string):
    if len(string)==1:
        return [string]
    all_perms = set()
    N = len(string)
    char = string[-1]
    perm = permutations(string[:-1])
    for p in perm:
        p = list(p)
        for i in range(N):
            p[i:i] = char
            all_perms.add(''.join(p))
            p.pop(i)
    return list(all_perms)
