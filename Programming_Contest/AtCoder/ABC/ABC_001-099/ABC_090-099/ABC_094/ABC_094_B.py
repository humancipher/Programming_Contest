from bisect import bisect_left

N,M,X = map(int,input().split())
A = list(map(int,input().split()))

left = bisect_left(A,X)
right = M - left

print(min(left,right))
