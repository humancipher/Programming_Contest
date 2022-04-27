from math import ceil

N,M = map(int,input().split())
name = input()
kit = input()

KIT = set()
for i in range(M):
    if kit[i] not in KIT:
        KIT.add(kit[i])

ans,l = 0,0
for k in KIT:
    ans = max(ans,ceil(name.count(k)/kit.count(k)))
    l += name.count(k)

if N != l:
    print(-1)
else:
    print(ans)
