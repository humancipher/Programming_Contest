N = int(input())

ans = 0
for a in range(1,N):
    if a**2 < N:
        ans += 1
    for b in range(a+1,N):
        if a * b < N:
            ans += 2
        else:
            break

print(ans)
