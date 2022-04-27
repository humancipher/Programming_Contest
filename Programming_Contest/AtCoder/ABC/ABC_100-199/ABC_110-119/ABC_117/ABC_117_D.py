n,k = map(int,input().split())
A = list(map(int,input().split()))

AB = [0] * 60
for i in range(n):
    a = A[i]
    for j in range(60):
        AB[j] += a % 2
        a //= 2

x = 0
for j in reversed(range(60)):
    if AB[j]*2 <= n and x + 2**j <= k:
        x += 2**j

ans = 0
for i in range(n):
    ans += x ^ A[i]
print(ans)