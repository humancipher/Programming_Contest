n = int(input())
t = 0
AB = []
for _ in range(n):
    a,b = map(int,input().split())
    AB.append([a,b])
    t += a/b
t_col = t/2
ans = 0
while t_col > 0:
    for i in range(n):
        a,b = AB[i][0],AB[i][1]
        if t_col > a/b:
            t_col -= a/b
            ans += a
        else:
            ans += b * t_col
            t_col = 0
print(ans)
