import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
lis = {}
string = ""
lis2 = []
lis3 = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.

    #Fill the hashmap.
    ext, mt = input().split()
    lis[ext.lower()] = mt
# print(lis)
for i in range(q):
    fname = input()  # One file name per line.
    # print(fname)
    ext = fname.rfind(".")
    if ext < 0:
        exti = ""
    else:
        exti = (fname[ext + 1:].lower())

    if exti in lis:
        print(lis[exti])
    else:
        print("UNKNOWN")






# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
for i in range(len(lis2)):
    print(lis2[i])  
