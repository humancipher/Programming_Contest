N = int(input())
B = list(map(int,input().split()))

A = [B[i] for i in range(N-1)]

for i in range(N-2):
    if max(A[i],A[i+1]) > B[i]:
        A[i+1] = B[i]
A.append(B[N-2])

print(sum(A))
