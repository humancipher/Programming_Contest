n,m = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
for i in range((n+1)//2):
    A[n-i],A[i] = A[i],A[n-i]
for i in range((n+m+1)//2):
    C[n+m-i],C[i] = C[i],C[n+m-i]
B =  list()
for i in range(m+1):
    d = C[i]//A[0]
    B.append(d)
    for j in range(n+1):
        C[i+j] -= d * A[j]
for i in range((m+1)//2):
    B[m-i],B[i] = B[i],B[m-i]
print(" ".join(map(str,B)))