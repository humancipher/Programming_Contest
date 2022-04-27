A = [int(input()) for _ in range(5)]
k = int(input())

if A[-1] - A[0] > k:
    print(":(")
else:
    print("Yay!")
