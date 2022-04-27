N = 4*10**6
a = [1,2]

pt,tmp = 2,3
while tmp < N:
    tmp = a[pt-1]+a[pt-2]
    a.append(tmp)
    pt += 1

ans = 0
for i in range(pt-1):
    if a[i] % 2 == 0:
        ans += a[i]

print(ans)
