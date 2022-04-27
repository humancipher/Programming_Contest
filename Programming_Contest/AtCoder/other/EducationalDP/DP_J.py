def rec(dp,n,i,j,k):
    if dp[i][j][k] != None:
        return dp[i][j][k]
    else:
        base = i+j+k #i=0⋀j=0⋀k=0の場合はdp[0][0][0]を指定済
        pi,pj,pk = 0,0,0
        if i > 0:
            pi = (rec(dp,n,i-1,j,k) * i) / base
        if j > 0:
            pj = (rec(dp,n,i+1,j-1,k) * j) / base
        if k > 0:
            pk = (rec(dp,n,i,j+1,k-1) * k) / base
        if base == n:
            dp[i][j][k] = pi + pj + pk + 1
        else:
            dp[i][j][k] = pi + pj + pk + n / base
        return dp[i][j][k]

n = int(input())
A = list(map(int,input().split()))
    
C = [0,0,0] #C[i]:i+1個皿の枚数
for i in range(n):
    C[A[i]-1] += 1
dp = [[[None] * (n+1) for _ in range(n+1)] for _ in range(n+1)] #dpをメインルーチンから外さないとグローバル変数にならずメモ化されない
dp[0][0][0] = 0
print(rec(dp,n,C[0],C[1],C[2]))
