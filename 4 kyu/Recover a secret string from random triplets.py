# Description #

# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. 
# "whi" is a triplet for the string "whatisup".

# As a simplification, you may assume that no letter occurs more than once in the secret string.

# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. 
# In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.



def recoverSecret(triplets):
    ret = list(set(char for triplet in triplets for char in triplet))
    for _ in range(len(ret)):
        amend = False
        for triplet in triplets:
            idx1, idx2, idx3 = map(lambda x: ret.index(x), triplet)
            if idx1 > idx2:
                ret[idx1], ret[idx2] = ret[idx2], ret[idx1]
                idx1, idx2 = idx2, idx1
                amend = True
            if idx2 > idx3:
                ret[idx2], ret[idx3] = ret[idx3], ret[idx2]
                idx2, idx3 = idx3, idx2
                amend = True
            if idx1 > idx3:
                ret[idx1], ret[idx3] = ret[idx3], ret[idx1]
                idx1, idx3 = idx3, idx1
                amend = True
        if amend == False:
            break
    return ''.join(ret)
