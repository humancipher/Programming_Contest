T = int(input())
LR = [list(map(int,input().split())) for _ in range(T)]

for i in range(T):
    l,r = LR[i][0],LR[i][1]
    if r >= 2*l:
        ans = (r-2*l+1)*(r-2*l+2)//2
    else:
        ans = 0
    print(ans)
