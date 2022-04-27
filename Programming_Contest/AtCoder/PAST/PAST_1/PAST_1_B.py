N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(1,N):
    if A[i] == A[i-1]:
        print("stay")
    elif A[i] > A[i-1]:
        print("up",A[i]-A[i-1])
    else:
        print("down",A[i-1]-A[i])
