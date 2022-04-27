n = int(input())
B = [int(input()) for _ in range(n)]
A = [None] * n
A[0] = 0
for i in range(1,n):
    A[i] = A[i-1] ^ B[i-1]
if A[n-1] == B[n-1]:
    for i in range(n):
        print(A[i])
else:
    print(-1)
