x = 1
y  = 1

NORTH = "n"
SOUTH = "s"
WEST = "w"
EAST ="e"

#possible directions
p_North = "(N)orth"
p_NorthOrEastOrWest = "(N)orth or (E)ast or (S)outh"
p_EastOrSouth = "(E)ast or (S)outh"
p_SouthOrWest = "(S)outh or (W)est"
p_WestOrEast = "(W)est or (E)ast" 
p_NorthOrSouth = "(S)outh or (N)orth"

isValid = True

def getPossibleDirections(x, y):
    if (x is 1 and y is 1 ) or (x is 2 and y is 1):
        return p_North

    if x is 1 and y is 2:
        return p_NorthOrEastOrWest

    if x is 1 and y is 3:        
        return p_EastOrSouth

    if (x is 2 and y is 2) or (x is 3 and y is 3):
        return p_SouthOrWest

    if x is 2 and y is 3:
        return p_WestOrEast 

    if x is 3 and y is 2:
        return p_NorthOrSouth

def isPossibleDirection(direction):
    return direction == NORTH or direction == EAST or direction == SOUTH or direction == WEST

def isValidDirection(direction):
    if not isPossibleDirection(direction):
        return False

    possible_directions = getPossibleDirections(x, y)

    if possible_directions == p_North:
        if direction != NORTH:
            return False

    elif possible_directions == p_NorthOrEastOrWest:
        if direction != EAST and direction != SOUTH and direction != NORTH:
            return False

    elif possible_directions == p_EastOrSouth:       
        if direction != EAST and direction != SOUTH:
            return False

    elif possible_directions == p_SouthOrWest:
        if direction != SOUTH and direction != WEST:
            return False

    elif possible_directions == p_WestOrEast: 
        if direction != EAST and direction != WEST:
            return False

    elif possible_directions == p_NorthOrSouth:
        if direction != NORTH and direction != SOUTH:
            return False

    return True


while x != 3 or y != 1: 

    if isValid == True:
        print("You can travel: ", getPossibleDirections(x, y))
    move = input("Direction: ")

    isValid = isValidDirection(move.lower())

    if isValid == True:
        if move.lower()== NORTH and y < 3:
            y +=1
        elif move.lower()== SOUTH and y > 1:
            y -=1     
        elif move.lower()== WEST and x > 1:
            x -=1
        elif move.lower() == EAST and x < 3:
            x +=1
        else:
            isValid = False


    if isValid == False:
        print("Not a valid direction")


else:
    print("Victory!")






    




















