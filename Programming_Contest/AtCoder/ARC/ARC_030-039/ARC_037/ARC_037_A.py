n = int(input())
M = list(map(int,input().split()))

ans = 0
for m in M:
    ans += max(0,80-m)
print(ans)
