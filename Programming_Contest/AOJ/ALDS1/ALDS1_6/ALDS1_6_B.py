N = int(input())
A = [int(x) for x in input().split()]

def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

p = Partition(A,0,N-1)

for i in range(N):
    if i != 0:
        print(" ",end="")
    if i == p:
        print("[",end="")
    print(A[i],end="")
    if i == p:
        print("]",end="")
print()
