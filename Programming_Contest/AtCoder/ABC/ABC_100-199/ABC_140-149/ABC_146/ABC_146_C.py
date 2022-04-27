A, B, X = map(int, input().split())

def deg(N):
    count = 0
    while N > 0:
        N = N // 10
        count += 1
    return count

def binsearch(A,B,X,Nsmall,Nbig):
    if A*(10**9)+B*deg(10**9) <= X:
        return 10**9
    else:
        mid = (Nsmall+Nbig)//2
        if Nsmall > Nbig:
            return 0
        elif A*mid + B*deg(mid) <= X and A*(mid+1) + B*deg(mid+1) > X:
            return mid
        elif A*mid + B*deg(mid) < X:
            return binsearch(A,B,X,mid+1,Nbig)
        elif A*mid + B*deg(mid) > X:
            return binsearch(A,B,X,Nsmall,mid-1)

print(binsearch(A,B,X,1,10**9))
