from bisect import bisect_left

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

INF = 10**10
B.append(-INF)
B.append(INF)
A.sort()
B.sort()
ans = INF
for a in A:
    bl = bisect_left(B,a)
    ans = min(ans,B[bl]-a,a-B[bl-1])
print(ans)
