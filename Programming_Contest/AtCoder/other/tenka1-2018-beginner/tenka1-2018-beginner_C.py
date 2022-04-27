n = int(input())
A = [int(input()) for _ in range(n)]

A.sort()
B = [0] * n
C = [0] * n
for i in range(n-1):
    if i % 2 == 0:
        B[i+1] += 1
        B[i] -= 1
        C[i+1] -= 1
        C[i] += 1
    else:
        B[i+1] -= 1
        B[i] += 1
        C[i+1] += 1
        C[i] -= 1
B.sort()
C.sort()

ans1,ans2 = 0,0
for i in range(n):
    ans1 += A[i] * B[i]
    ans2 += A[i] * C[i]
print(max(ans1,ans2))