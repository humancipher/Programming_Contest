INF = 2*10**9+1

H = int(input())
Heap = [-INF]
Heap += list(map(int,input().split()))

def maxHeapify(A,i):
    if i>= 1:
        l,r = i*2,i*2+1
        if l > len(A)-1:
            l,r = 0,0
        elif r > len(A)-1:
            r = 0
        if A[i] <= A[l] and A[r] <= A[l]:
            largest = l
        if A[l] <= A[r] and A[i] <= A[r]:
            largest = r
        if A[l] <= A[i] and A[r] <= A[i]:
            largest = i

        if largest != i and largest != 0:
            A[i],A[largest] = A[largest],A[i]
            maxHeapify(A,largest)

def buildMaxHeap(A):
    for i in reversed(range(1,(len(A)-1)//2+1)):
        maxHeapify(A,i)

buildMaxHeap(Heap)
print(""," ".join(map(str,Heap[1:H+1])))
