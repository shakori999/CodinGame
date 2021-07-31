import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
row = []
grid = []
n = int(input())
l = int(input())
for i in range(n):
    for cell in input().split():
        row.append(cell)
        if len(row) == n:
            grid.append(row)
            row = []


for i in range(n):
    for j in range(n):
        if grid[i][j] == "C":
            grid[i][j] = l
        else:
            grid[i][j] = 0

for i in range(l - 1, 0 , -1):
    for x in range(n):
        for y in range(n):
            max_surr = 0
            for x_step in range(-1, 2):
                for y_step in range(-1, 2):
                    if 0 <= x + x_step < n and 0 <= y + y_step < n:
                        max_surr = max(max_surr, grid[x + x_step][y + y_step])
            grid[x][y] = max(grid[x][y], max_surr - 1)

print(sum(x.count(0) for x in grid))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

