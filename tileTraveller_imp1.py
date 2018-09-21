x = 1
y  = 1

NORTH = "n"
SOUTH = "s"
WEST = "w"
EAST ="e"


possible_directions = "(N)orth."
isValid = True


while x != 3 or y != 1: 

    if isValid == True:
        print("You can travel:", possible_directions)
    move = input("Direction: ")
    isValid = True

    if (x is 1 and y is 1 ) or (x is 2 and y is 1):
        if move.lower() != NORTH:
            isValid = False

    elif x is 1 and y is 2:
        if move.lower() != EAST and move.lower() != SOUTH and move.lower() != NORTH:
            isValid = False

    elif x is 1 and y is 3:        
        if move.lower() != EAST and move.lower() != SOUTH:
            isValid = False

    elif (x is 2 and y is 2) or (x is 3 and y is 3):
        if move.lower() != SOUTH and move.lower() != WEST:
            isValid = False

    elif x is 2 and y is 3: 
        if move.lower() != EAST and move.lower() != WEST:
            isValid = False

    elif x is 3 and y is 2:
        if move.lower() != NORTH and move.lower() != SOUTH:
            isValid = False

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

    if (x is 1 and y is 1 ) or (x is 2 and y is 1):
        possible_directions = "(N)orth."

    elif x is 1 and y is 2:
        possible_directions = "(N)orth or (E)ast or (S)outh."

    elif x is 1 and y is 3:        
        possible_directions = "(E)ast or (S)outh."

    elif (x is 2 and y is 2) or (x is 3 and y is 3):
        possible_directions = "(S)outh or (W)est."

    elif x is 2 and y is 3:
        possible_directions = "(E)ast or (W)est." 

    elif x is 3 and y is 2:
        possible_directions ="(N)orth or (S)outh."


    if isValid == False:
        print("Not a valid direction!")


else:
    print("Victory!")






    




















