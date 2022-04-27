N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(N-1):
    A[i+1] = max(A[i],A[i+1])

M = 0
for i in range(N):
    if M < A[i] * B[i]:
        M = A[i] * B[i]
    print(M)
