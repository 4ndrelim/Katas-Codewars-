# Description #

# The keypad has the following layout:
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# The spy noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). 
# E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. 
# That's why we can try out all possible (*) variations.
# Note: * possible in sense of: the observed PIN itself and all variations considering the adjacent digits

# Find a function that returns an array of all variations for an observed PIN with a length of 1 to 8 digits. 
# Note: All PINs, the observed one and also the results, must be strings, because of potentially leading '0's. 

  
  
key = {'1': ['1','2','4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'],
       '4': ['1','4','5','7'], '5': ['2','4','5','6','8'], '6': ['3','5','6','9'],
       '7': ['4','7','8'], '8': ['5','7','8','9','0'], '9': ['6','8','9'], '0': ['0','8'] }

def get_pins(observed):
    make_complete = key[observed[0]]
    for char in observed[1:]:
        partial = []
        for pos in key[char]:
            for string in make_complete:
                string+=pos
                partial.append(string)
        make_complete = partial
    return make_complete

def get_pins(observed): #backtrack
    all_poss, string = [], ""
    def helper(rem):
        nonlocal string
        if not rem:
            all_poss.append(string)
            return
        for char in key[rem[0]]:
            string+=char
            helper(rem[1:])
            string = string[:-1]
    helper(observed)
    return all_poss
