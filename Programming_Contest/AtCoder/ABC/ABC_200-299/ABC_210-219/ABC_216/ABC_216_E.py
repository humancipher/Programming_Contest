def bound(ue,sita,yoko,k):
    #(ue-x)*yoko <= kになるxの最大値
    left,right = sita-1,ue
    while right - left > 1:
        mid = (left+right)//2
        if (ue-mid) * yoko <= k:
            right = mid
        else:
            left = mid
    return right

n,k = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)
A += [0]
S = 0
for i in range(n):
    S += A[i]*(A[i]+1)//2
if k >= S:
    ans = S
else:
    pt,ans = 0,0
    while k > 0 and pt < len(A)-1:
        tmp = (A[pt]-A[pt+1])*(pt+1)
        if k >= tmp:
            ans += (A[pt]*(A[pt]+1)//2 - A[pt+1]*(A[pt+1]+1)//2)*(pt+1)
            k -= tmp
        else:
            b = bound(A[pt],A[pt+1],pt+1,k)
            ans += (A[pt]*(A[pt]+1)//2 - b*(b+1)//2) * (pt+1)
            k -= (A[pt]-b)*(pt+1)
            if k > 0:
                ans += b*k
                k = 0
        pt += 1
print(ans)
