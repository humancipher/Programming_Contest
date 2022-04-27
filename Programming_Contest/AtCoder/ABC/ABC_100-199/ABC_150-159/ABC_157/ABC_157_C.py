N,M = map(int,input().split())
SC = [list(map(int,input().split())) for _ in range(M)]

NUM = [-1 for _ in range(N)]

flag = 0
for i in range(M):
    if NUM[SC[i][0]-1] == -1:
        NUM[SC[i][0]-1] = SC[i][1]
    elif NUM[SC[i][0]-1] != SC[i][1]:
        flag = 1
        break
if NUM[0] == -1:
    if N == 1:
        NUM[0] = 0
    else:
        NUM[0] = 1

ans = 0
for i in range(N):
    if NUM[i] != -1:
        ans += NUM[i]*10**(N-i-1)

if flag == 1 or (NUM[0] == 0 and N != 1):
    print(-1)
else:
    if NUM[0] == -1:
        print(ans+10**(N-1))
    else:
        print(ans)
