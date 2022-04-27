def judge(ABCDE,x):
    P = set()
    for a,b,c,d,e in ABCDE:
        pat = (a >= x,b >= x,c >= x,d >= x,e >= x)
        if pat not in P:
            P.add(pat)
    ans = False
    for p1 in P:
        for p2 in P:
            for p3 in P:
                a = p1[0] or p2[0] or p3[0]
                b = p1[1] or p2[1] or p3[1]
                c = p1[2] or p2[2] or p3[2]
                d = p1[3] or p2[3] or p3[3]
                e = p1[4] or p2[4] or p3[4]
                ans |= a and b and c and d and e
    return ans

def solve(ABCDE):
    l,r = 0,10**9+1
    while r - l > 1:
        mid = (r+l)//2 #judge(ABCDE,l) <= judge(ABCDE,mid) < judge(ABCDE,r)
        if judge(ABCDE, mid):
            l = mid
        else:
            r = mid
    return l

n = int(input())
ABCDE = [list(map(int,input().split())) for _ in range(n)]
print(solve(ABCDE))
