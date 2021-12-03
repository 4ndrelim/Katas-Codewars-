# Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly

# The data structure is a multi-dimensional Array

# Rules:
# 1. Data structure dimension: NxN where N > 0 and √N == integer
# 2. Rows may only contain integers: 1..N (N included)
# 3. Columns may only contain integers: 1..N (N included)
# 4. 'Little squares' may also only contain integers: 1..N (N included)


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.small = int(self.size**0.5)
    
    def is_valid(self):
        #if self.small % 1 != 0:
            #return False
        for i in range(self.size):
            
            #check ith row
            idx = [False for _ in range(self.size)]
            for num in self.data[i]:
                if type(num) == int and 0<=num-1<self.size:
                    idx[num-1] = True
                else:
                    return False
            if any(idx[j] == False for j in range(self.size)):
                return False
            
            #check ith col
            idx = [False for _ in range(self.size)]
            for row in self.data:
                if type(num) == int and 0<=num-1<self.size:
                    idx[row[i]-1] = True
                else:
                    return False
            if any(idx[j] == False for j in range(self.size)):
                return False
            
            #check ith little box:
            idx = [False for _ in range(self.size)]
            r = i//self.small * self.small #find index of the first row of the jth layer
            c = i%self.small * self.small #find index of first col of the jth layer (vert). boxes of jth col is congruent to j mod n
            for j in range(self.small):
                for k in range(self.small):
                    num = self.data[r+j][c+k]
                    if type(num) == int and 0<=num-1<self.size:
                        idx[num-1] = True
                    else:
                        return False
            if any(idx[j] == False for j in range(self.size)):
                return False
            
        return True #pass all checks
