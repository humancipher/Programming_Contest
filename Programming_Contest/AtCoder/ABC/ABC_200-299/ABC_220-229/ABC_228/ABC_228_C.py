from bisect import bisect_left

n,k = map(int,input().split())
P,Q = [],[]
for i in range(n):
    a,b,c = map(int,input().split())
    P.append(a+b+c)
    Q.append(a+b+c)    

Q.sort()
for i in range(n):
    if bisect_left(Q,P[i]+301) >= n-k+1:
        print("Yes")
    else:
        print("No")
