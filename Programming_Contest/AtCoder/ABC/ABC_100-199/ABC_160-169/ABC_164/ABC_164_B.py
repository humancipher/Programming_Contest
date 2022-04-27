a,b,c,d = map(int,input().split())

turn = 0
while a > 0 and c > 0:
    if turn == 0:
        c -= b
    else:
        a -= d
    turn = (turn + 1) % 2

if a > 0:
    print("Yes")
else:
    print("No")
