from math import pi

L = list(map(int,input().split()))
L.sort()

if L[-1] <= L[0] + L[1]:
    ans = pi * sum(L)**2
else:
    ans = pi * (sum(L)**2 - (L[-1] - L[0] - L[1])**2)

print(ans)
