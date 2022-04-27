n = int(input())
A = list(map(int,input().split()))
B = [False] * 2002
for i in range(n):
    B[A[i]] = True
for i in range(2002):
    if not B[i]:
        print(i)
        break