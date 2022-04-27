c = [list(map(int,input().split())) for _ in range(3)]

a = [None for _ in range(3)]
b = [None for _ in range(3)]

b[0],a[0]=0,c[0][0]

for i in range(1,3):
    a[i] = c[0][i]-b[0]
for j in range(1,3):
    b[j] = c[j][0]-a[0]

ans = "Yes"
for i in range(3):
    for j in range(3):
        if c[i][j] != a[j]+b[i]:
            ans = "No"
            break

print(ans)
