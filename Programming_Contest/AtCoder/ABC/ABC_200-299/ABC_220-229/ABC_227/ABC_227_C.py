n = int(input())

ans = 0
for a in range(1,int(pow(n,1/3))+2):
    m = n // a
    for b in range(a,int(pow(m,1/2))+2):
        c = m // b
        if a*b*c <= n and b <= c:
            ans += c-b+1
print(ans)
