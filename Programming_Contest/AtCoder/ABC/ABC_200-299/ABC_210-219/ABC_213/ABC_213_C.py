from bisect import bisect_left

H,W = set(),set()
h,w,n = map(int,input().split())
AB = list()
for _ in range(n):
    a,b = map(int,input().split())
    AB.append([a-1,b-1])
    H.add(a-1)
    W.add(b-1)
H = list(H)
W = list(W)
H.sort()
W.sort()
Ans = list()
for a,b in AB:
    x = bisect_left(H,a)
    y = bisect_left(W,b)
    Ans.append([x+1,y+1])
for i in range(len(Ans)):
    print(" ".join(map(str,Ans[i])))