s,t = map(int,input().split())
ans = 0
for a in range(s+1):
    for b in range(s-a+1):
        for c in range(s-a-b+1):
            if a*b*c <= t:
                ans += 1
print(ans)
