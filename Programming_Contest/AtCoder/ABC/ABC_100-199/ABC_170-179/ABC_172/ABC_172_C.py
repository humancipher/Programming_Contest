from bisect import bisect_right

N,M,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(1,len(A)):
    A[i] += A[i-1]

for i in range(1,len(B)):
    B[i] += B[i-1]

A = [0] + A
B = [0] + B

ans = 0
for i in range(len(A)):
    if K - A[i] > 0:
        ans = max(ans,i + bisect_right(B,K - A[i]) - 1)

for i in range(len(B)):
    if K - B[i] > 0:
        ans = max(ans,i + bisect_right(A,K - B[i]) - 1)

print(ans)
