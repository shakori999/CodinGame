import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
row = []

maze = []
width, height = [int(i) for i in input().split()]
for i in range(height):
    line = input()
    maze.append(list(line))
    
def count(h, w):
    walls = 0
    try:
        if w != width and maze[h][w + 1] != "#":
            walls += 1
    except:
        pass
    try :
        if w != 0 and maze[h][w - 1] != "#":
            walls += 1
    except:
        pass
    try:
        if h != height and maze[h + 1][w] != "#":
            walls += 1
    except:
        pass
    try:
        if h != 0 and maze[h - 1][w] != "#":
            walls += 1
    except:
        pass

    
    return walls  

for i in range(height):
    for j in range(width):
        if maze[i][j] == "#":
            print("#", end="")
        else:
            print(count(i, j), end="")
    print("") 
 
# for i in range(height):
#     # print("maze")
#     print(maze[i])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
   