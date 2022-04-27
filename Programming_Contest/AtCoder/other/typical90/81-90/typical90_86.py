from re import X
from sys import stdin
input = stdin.readline
mod = 10**9+7

n,q = map(int,input().split())
XYZW = [list(map(int,input().split())) for _ in range(q)]
ans = 1
for a in range(60):
    tmp = 0
    for b in range(1<<n):
        flag = True
        for x,y,z,w in XYZW:
            if ((b>>(x-1)) % 2 | (b>>(y-1)) % 2| (b>>(z-1)) % 2) != (w>>a) % 2:
                flag = False
                break
        if flag:
            tmp += 1
    ans *= tmp
    ans %= mod
print(ans)