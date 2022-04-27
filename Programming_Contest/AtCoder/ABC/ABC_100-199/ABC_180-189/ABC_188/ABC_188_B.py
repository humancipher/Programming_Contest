N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

pro = 0
for i in range(N):
    pro += A[i] * B[i]

if pro == 0:
    print("Yes")
else:
    print("No")
