n = int(input())
TLR = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    if TLR[i][0] == 2:
        TLR[i][2] -= 0.1
    if TLR[i][0] == 3:
        TLR[i][1] += 0.1
    if TLR[i][0] == 4:
        TLR[i][1] += 0.1
        TLR[i][2] -= 0.1

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if TLR[i][1] <= TLR[j][2] and TLR[j][1] <= TLR[i][2]:
            ans += 1
print(ans)
