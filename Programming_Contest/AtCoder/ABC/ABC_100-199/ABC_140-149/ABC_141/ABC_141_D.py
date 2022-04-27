import heapq
from math import ceil

N, M = map(int, input().split())
A = [(-1)*int(x) for x in input().split()]

if len(A) == 1:
    for i in range(M):
        A[0] = ceil(A[0]/2)
    A[0] = -A[0]
    print(A[0])
else:
    count = 0
    heapq.heapify(A)
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    while count < M:
        while a <= b:
            a = ceil(a/2)
            count += 1
            if count == M:
                break
        if count == M:
            break
        heapq.heappush(A,a)
        a = b
        b = heapq.heappop(A)
    heapq.heappush(A,a)
    heapq.heappush(A,b)
    ans = (-1)*sum(A)
    print(ans)
