N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]

cnt,cnt_max = 0,0
for i in range(N):
    if D[i][0] == D[i][1]:
        cnt += 1
    else:
        cnt = 0
    cnt_max = max(cnt,cnt_max)

if cnt_max >= 3:
    print("Yes")
else:
    print("No")
