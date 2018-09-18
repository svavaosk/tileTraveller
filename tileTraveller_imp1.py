#The player starts in tile (1,1). At the beginning, and after each move selected by the player, the
#program should print the player’s travel options. If there is an open wall in a direction, write that
#direction as a possible travel direction.

positions : possible_directions
(1,1) : (N)orth
(1,2) : (N)orth,  (E)ast, (S)outh,
(1,3) : (E)ast, (S)outh
(2,1) : (N)orth
(2,2) : (S)outh, (W)est
(2,3) : (W)est, (E)ast 
(3,1) : (N)orht
(3,2) : (S)outh, (N)orth 
(3,3) : (S)outh, (W)est 

if position is (1,1):
    possible_direction = (N)orth
elif position is (1,2):
    possible_direction = (N)orth or  (E)ast or (S)outh
elif position is (1,3):
    possible_direction = (E)ast or (S)outh
elif position is (2,1):
    possible_direction = (N)orth
elif position is (2,2):
    possible_direction = (S)outh or (W)est
elif position is ()
print("You can travel: ", possible_directions)
print("Direction: "input_direction)
print("Not a valid direction")




starting_point = (1,1)







output:
You can travel: (N)orth.
Direction: s
Not a valid direction!
Direction: n
You can travel: (N)orth or (E)ast or (S)outh.
Direction: N
You can travel: (E)ast or (S)outh.
Direction: w
Not a valid direction!
Direction: E
You can travel: (E)ast or (W)est.
Direction: e
You can travel: (S)outh or (W)est.
Direction: s
You can travel: (N)orth or (S)outh.
Direction: S
Victory!