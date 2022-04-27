N = int(input())
A = list(map(int,input().split()))

Ans = [0 for _ in range(N)]

for i in range(N):
    if i % 2 == 0:
        Ans[0] += A[i]
    else:
        Ans[0] -= A[i]

for i in range(1,N):
    Ans[i] = 2*A[i-1] - Ans[i-1]

print(" ".join(map(str,Ans)))
