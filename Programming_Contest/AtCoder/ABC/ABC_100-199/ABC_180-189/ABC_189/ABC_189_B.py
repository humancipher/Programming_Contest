N,X = map(int,input().split())
VP = [list(map(int,input().split())) for _ in range(N)]

alc = 0
X *= 100

ans = 1
for i in range(N):
    alc += VP[i][0] * VP[i][1]
    if alc > X:
        break
    else:
        ans += 1

if ans == N+1:
    print(-1)
else:
    print(ans)
