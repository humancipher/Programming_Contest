N = int(input())
ans = 1
while ans**2 <= N:
    ans += 1
ans -= 1

print(ans**2)
