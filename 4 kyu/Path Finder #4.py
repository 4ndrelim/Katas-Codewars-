# Description #
# Hey, Path Finder, where are you?

# Personal Note: This kata is an interesting puzzle that requires you to deduce 'your location' from the given test cases


x,y = 0,0  #start
D = 0  #tracks direction
dir = {'r': 1, 'R': 2, 'l': 3, 'L': 2}  #uncapitalized letters represent clockwise/anti-clockwise 90deg shift. Capitalized letters rep 180 deg shift
def i_am_here(path):
    global D, x, y  #answers to subsequent test cases built from previous ones
    path = list(path)
    path.reverse()  #to allow simply popping of last element which is O(1)
    while path:
        char = path.pop()
        if char in dir:
            D+=dir[char]
            D%=4
        else:
            step = int(char)
            while path and path[-1] not in dir:
                step*=10
                step+=int(path.pop())
            if D == 0:
                y-=step
            elif D == 1:
                x+=step
            elif D == 2:
                y+=step
            else:
                x-=step
    return [y,x]
