import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
players = []
rowls = {
    "C": ["P", "L"],
    "P": ["R", "S"],
    "R": ["L", "C"],
    "L": ["S", "P"],
    "S": ["C", "R"],
}
n = int(input())
for i in range(n):
    numplayer, signplayer = input().split()
    numplayer = int(numplayer)
    player = {
        "num": numplayer,
        "sign": signplayer,
        "lose": False,
        "wins": []
    }
    players.append(player)

def match(rowls, player_num, i):
    a = players[i]["sign"]
    b = players[i + 1]["sign"]
    if a in rowls[b]:
        player_num[i]["lose"] = True
        loser = i
        player_num[i + 1]["wins"].append(str(player_num[i]["num"]))
    elif b in rowls[a]:
        player_num[i + 1]["lose"] = True
        loser = i + 1
        player_num[i]["wins"].append(str(player_num[i+ 1]["num"]))
    elif a == b:
        if player_num[i]["num"] > player_num[i + 1]["num"]:
            player_num[i]["lose"] = True
            loser = i
            player_num[i + 1]["wins"].append(str(player_num[i]["num"]))
        elif player_num[i]["num"] < player_num[i + 1]["num"]:
            player_num[i + 1]["lose"] = True
            loser = i + 1
            player_num[i]["wins"].append(str(player_num[i + 1]["num"]))
    return player_num, loser

while len(players) > 1:
    loserse = []
    for i in range(0, len(players), 2):
        loser = 0
        players, loser = match(rowls, players, i) 
        loserse.append(loser)

    for i in loserse[::-1]:
        players.pop(i) 

print(players[0]["num"])
print(" ".join(players[0]["wins"]))
     
    # Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)




# print()