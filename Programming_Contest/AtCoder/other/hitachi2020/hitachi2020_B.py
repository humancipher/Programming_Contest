a,b,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
XYC = [list(map(int,input().split())) for i in range(m)]

kouho = (min(A)+min(B))
for i in range(m):
    kouho = min(kouho,A[XYC[i][0]-1] + B[XYC[i][1]-1] - XYC[i][2])

print(kouho)
