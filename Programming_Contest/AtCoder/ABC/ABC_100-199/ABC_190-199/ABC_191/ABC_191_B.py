N,X = map(int,input().split())
A = list(map(int,input().split()))

Ans = []
for i in range(N):
    if A[i] != X:
        Ans.append(A[i])

print(" ".join(map(str,Ans)))
