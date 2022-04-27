N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

V = []
for a,b in AB:
    V.append([a,b,2*a+b])

V.sort(key = lambda x : x[2],reverse=True)

ans = 0
aoki,takahashi = 0,0
for i in range(N):
    aoki += AB[i][0]

while aoki >= takahashi:
    aoki -= V[ans][0]
    takahashi += (V[ans][0] + V[ans][1])
    ans += 1

print(ans)
