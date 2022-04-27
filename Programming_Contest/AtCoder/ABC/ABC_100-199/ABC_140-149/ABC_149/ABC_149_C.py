import math

x = int(input())

def Eratos(n):
    P,L = [],[True for _ in range(n+1)]
    for i in range(2,int(math.sqrt(n))+1):
        if L[i]:
            for j in range(2,n//i+1):
                L[i*j] = False
    for i in range(2,n+1):
        if L[i]:
            P.append(i)
    return P

def b_search(A,key,left,right):
    mid = (left+right)//2
    if key <= A[0]:
        return A[0]
    elif key > A[len(A)-1]:
        return 10**9
    else:
        if A[mid] < key and key <= A[mid+1]:
            return A[mid+1]
        elif key > A[mid]:
            return b_search(A,key,mid,right)
        else:
            return b_search(A,key,left,mid)

P = Eratos(10**6)
ans = b_search(P,x,0,len(P))
print(ans)
