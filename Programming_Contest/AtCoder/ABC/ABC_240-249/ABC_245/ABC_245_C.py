n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

X = [[None,None] for _ in range(n)]
for i in range(n):
    X[i][0] = min(A[i],B[i])
    X[i][1] = max(A[i],B[i])
Y = [[False,False] for _ in range(n)]
Y[0] = [True,True]
for i in range(n-1):
    for j1 in range(2):
        if Y[i][j1]:
            for j2 in range(2):
                if abs(X[i][j1]-X[i+1][j2]) <= k:
                    Y[i+1][j2] = True
if Y[n-1][0] | Y[n-1][1]:
    print("Yes")
else:
    print("No")