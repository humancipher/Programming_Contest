n = int(input())
ans = "No"
beki,cnt = 1,0
while beki <= n**2 and cnt < n:
    beki *= 2
    cnt += 1
    if beki > n**2:
        ans = "Yes"
        break
print(ans)