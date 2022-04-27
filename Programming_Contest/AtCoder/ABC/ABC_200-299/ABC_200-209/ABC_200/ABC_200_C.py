n = int(input())
A = list(map(int,input().split()))

M = [0 for _ in range(200)]
for a in A:
    M[a % 200] += 1
ans = 0
for i in range(200):
    ans += M[i]*(M[i]-1) // 2
print(ans)
