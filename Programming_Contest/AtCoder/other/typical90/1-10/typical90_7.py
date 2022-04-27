from bisect import bisect_left

n = int(input())
A = list(map(int,input().split()))
q = int(input())
B = [int(input()) for _ in range(q)]

INF = 10**10
A.append(-INF)
A.append(INF)
A.sort()

for b in B:
    print(min(b - A[bisect_left(A,b)-1],A[bisect_left(A,b)] - b))
