N,K = map(int,input().split())
A = list(map(int,input().split()))

B = [0 for _ in range(N+1)] #B[i]:A[j] = iを満たすjの数

for i in range(N):
    B[A[i]] += 1

for i in range(len(B)-1):
    B[i+1] = min(B[i],B[i+1])

ans = 0
for i in range(N):
    ans += min(K,B[i])

print(ans)
