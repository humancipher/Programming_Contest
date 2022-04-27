def judge(A,n,k,score):
    tmp,cnt = A[0],0
    for i in range(1,n):
        if tmp < score:
            tmp += A[i]
        else:
            tmp = A[i]
            cnt += 1
    if cnt > k:
        return True
    elif cnt == k:
        return tmp >= score
    else:
        return False

def solve(A,l,n,k):
    last = l - A[-1]
    for i in reversed(range(1,n)):
        A[i] -= A[i-1]
    A.append(last)
    left,right = 0,l
    while right - left > 1:
        mid = (left+right)//2
        if judge(A, n+1, k, mid):
            left = mid
        else:
            right = mid
    return left

n,l = map(int,input().split())
k = int(input())
A = list(map(int,input().split()))
print(solve(A, l, n, k))
