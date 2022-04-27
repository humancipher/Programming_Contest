def judge(A,p,k):
    cnt = 0
    for a in A:
        cnt += min(a,p)
    return cnt >= p*k

n,k = map(int,input().split())
A = list(map(int,input().split()))
left,right = 0,sum(A)+1
while right - left > 1:
    mid = (left+right)//2
    if judge(A,mid,k):
        left = mid
    else:
        right = mid
print(left)
