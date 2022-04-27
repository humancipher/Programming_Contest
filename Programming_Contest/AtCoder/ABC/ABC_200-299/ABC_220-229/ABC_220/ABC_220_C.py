def b_search(sa,x):
    left,right = 0,10**19 #sa*left <= x and sa *right > x
    while right - left > 1:
        mid = (left+right)//2
        if sa * mid <= x:
            left = mid
        else:
            right = mid
    return left

n = int(input())
A = list(map(int,input().split()))
x = int(input())

sa = sum(A)
q = b_search(sa,x)
x -= sa * q
r = 0
for i in range(n):
    if x >= A[i]:
        x -= A[i]
    else:
        r = i+1
        break
print(q*n+r)
