H,W,X,Y = map(int,input().split())
S = [list(input()) for _ in range(H)]
X -= 1
Y -= 1
Ans = set()
V = [(0,1),(0,-1),(1,0),(-1,0)]
for vx,vy in V:
    update = True
    k = 0
    while update:
        if 0 <= X+k*vx < H and 0 <= Y+k*vy < W:
            if S[X+k*vx][Y+k*vy] == ".":
                Ans.add((X+k*vx,Y+k*vy))
                k += 1
            else:
                update = False
                break
        else:
            update = False
            break
print(len(Ans))
