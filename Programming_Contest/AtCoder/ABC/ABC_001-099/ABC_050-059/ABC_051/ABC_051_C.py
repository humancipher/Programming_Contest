sx,sy,tx,ty = map(int,input().split())

S = ""
for k in range(2):
    if k == 1:
        S += "L"
    for i in range(ty-sy+k):
        S += "U"
    for i in range(tx-sx+k):
        S += "R"
    if k == 1:
        S += "DR"
    for i in range(ty-sy+k):
        S += "D"
    for i in range(tx-sx+k):
        S += "L"
    if k == 1:
        S += "U"

print(S)
