from math import gcd

l,r = map(int,input().split())
ans = 0
for x in range(l,min(l+10**3,r)):
    for y in range(max(l,r-10**3),r+1):
        if gcd(x,y) == 1:
            ans = max(ans,y-x)
print(ans)