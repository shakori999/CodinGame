import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

first = 0
second = 0
horses = []
result1 = 0
result2 = 10000000
n = int(input())
for i in range(n):
    pi = int(input())
    horses.append(pi)
horses.sort()

for i in range(1, n):
    second = horses[i-1]
    if second != first:
        first = second
        second = horses[i]
        result1 = second - first
        if result1 < result2:
            result2 = result1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result2)
