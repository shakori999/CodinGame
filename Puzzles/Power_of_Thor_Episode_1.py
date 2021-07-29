import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thorex = initial_tx
thorey = initial_ty
# game loop
while True:
    
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    dirx = ''
    diry = ''
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    if thorey > light_y:
        diry = 'N'
        thorey -= 1
    elif thorey < light_y:
        diry = 'S'
        thorey += 1
    
    if thorex <light_x:
        dirx = 'E'
        thorex += 1
    elif thorex > light_x:
        dirx = 'W'
        thorex -= 1

    dire = diry+dirx
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(dire)
