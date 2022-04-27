n,k = map(int,input().split())
S = [int(input()) for _ in range(n)]
ans = 0
ptl,ptr = 0,0
tmp = 1
if min(S) == 0:
    ans = n
elif min(S) <= k:
    while ptr < n:
        if tmp * S[ptr] <= k:
            tmp *= S[ptr]
            ans = max(ans,ptr-ptl+1)
            ptr += 1
        else:
            tmp //= S[ptl]
            ptl += 1
print(ans)
