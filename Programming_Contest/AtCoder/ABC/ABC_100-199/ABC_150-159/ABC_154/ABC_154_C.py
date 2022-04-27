N = int(input())
A = list(map(int,input().split()))

A = sorted(A)

flag = 0
for i in range(N-1):
    if A[i] == A[i+1]:
        flag = 1
        break

if flag == 0:
    print("YES")
else:
    print("NO")
