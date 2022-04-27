N = int(input())
A = list(map(int,input().split()))

flag = 0
for i in range(N):
    if A[i] % 2 == 0:
        if (A[i] % 3 != 0) and (A[i] % 5 != 0):
            flag = 1

if flag == 0:
    print("APPROVED")
else:
    print("DENIED")
