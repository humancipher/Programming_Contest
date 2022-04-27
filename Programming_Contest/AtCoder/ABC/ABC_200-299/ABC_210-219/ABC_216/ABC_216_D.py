#from heapq import heapify,heappush,heappop

n,m = map(int,input().split())
C = [set() for _ in range(n+1)] #C[i]:i番目の色がトップである筒の集合]
CL = [set() for _ in range(3)] #CL[i]:len(C[x]) == iであるxの集合
A = [[]]
for i in range(m):
    k = int(input())
    a = list(map(int,input().split()))
    for j in range(k//2):
        a[j],a[k-1-j] = a[k-1-j],a[j]
    C[a[k-1]].add(i+1)
    A.append(a)
for i in range(n+1):
    CL[len(C[i])].add(i)

ans = "Yes"
cnt = 0
while cnt < n:
    if len(CL[2]) > 0:
        for cl in CL[2]:
            tmp = cl
            break
        CL[2].discard(tmp)
        [x1,x2] = list(C[tmp])
        C[tmp].clear()
        A[x1].pop()
        A[x2].pop()
        y1,y2 = -1,-1
        if len(A[x1]) > 0:
            y1 = A[x1][-1]
        if len(A[x2]) > 0:
            y2 = A[x2][-1]
        if y1 == y2 and y1 != -1:
            C[y1].add(x1)
            C[y2].add(x2)
            CL[2].add(y1)
        else:
            if y1 != -1:
                C[y1].add(x1)
                if A[x1][-1] in CL[1]:
                    CL[1].discard(A[x1][-1])
                    CL[2].add(A[x1][-1])
                else:
                    CL[0].discard(A[x1][-1])
                    CL[1].add(A[x1][-1])
            if y2 != -1:
                C[y2].add(x2)
                if A[x2][-1] in CL[1]:
                    CL[1].discard(A[x2][-1])
                    CL[2].add(A[x2][-1])
                else:
                    CL[0].discard(A[x2][-1])
                    CL[1].add(A[x2][-1])
        cnt += 1
    else:
        ans = "No"
        break
print(ans)