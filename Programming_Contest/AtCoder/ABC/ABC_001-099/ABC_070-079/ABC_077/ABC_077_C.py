from bisect import bisect_left,bisect_right

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

#bisect_left:keyを挿入できる最小のindex
#bisect_right:keyを挿入できる最大のindex
ans = 0
for i in range(N):
    b_l,b_r = bisect_left(A,B[i]),N-bisect_right(C,B[i])
    ans += (b_l)*(b_r)
print(ans)
