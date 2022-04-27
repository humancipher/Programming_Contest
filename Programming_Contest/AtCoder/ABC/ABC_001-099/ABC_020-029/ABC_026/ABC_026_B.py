from math import pi

N = int(input())
R = [int(input()) for _ in range(N)]

R.sort(reverse = True)

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += R[i]**2
    else:
        ans -= R[i]**2

ans *= pi
print(ans)
