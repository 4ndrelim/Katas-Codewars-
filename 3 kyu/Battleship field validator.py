# Description #
# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. 
# Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

# Battleship (also Battleships or Sea Battle) is a guessing game for two players. 
# Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. 
# The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. 
# In this kata we will use Soviet/Russian version of the game

# Rules:
# 1. There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1) 
# 2. Any additional ships are not allowed, as well as missing ships.
# 3. Each ship must be a straight line, except for submarines, which are just single cell
# 4. The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner


def validate_battlefield(field):
    def no_contact():
        checks = [(-1,-1), (-1,1), (1,1), (1,-1)]
        for r in range(10):
            for c in range(10):
                for x,y in checks:
                    if field[r][c] == 1 and 0<=r+y<=9 and 0<=c+x<=9 and field[r+y][c+x] == 1:
                        return False
        return True
    
    def count_ship(ships):
        for row in range(10):
            for col in range(10):
                if 0<=row<9 and field[row+1][col] == 1:
                    field[row+1][col] += field[row][col]
                elif 0<=col<9 and field[row][col+1] == 1:
                    field[row][col+1] += field[row][col]
                elif field[row][col] > 0: #make sure there's a ship. Value at this cell will be the size of vert/hori ship
                    ships.append(field[row][col])
    
    if no_contact():
        ships, actual = [], [1,1,1,1,2,2,2,3,3,4]
        count_ship(ships)
        if sorted(ships) == actual:
            return True
    return False
