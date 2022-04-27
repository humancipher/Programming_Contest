N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [0] + A + [N+1]
N += 2
M += 2

A.sort()
W_list = []
min_W = N

for i in range(1,M):
    if A[i]-A[i-1] != 1:
        W_list.append(A[i]-A[i-1]-1)
        min_W = min(min_W,A[i]-A[i-1]-1)

ans = 0
for i in range(len(W_list)):
    ans += W_list[i] // min_W
    if W_list[i] % min_W != 0:
        ans += 1

print(ans)
