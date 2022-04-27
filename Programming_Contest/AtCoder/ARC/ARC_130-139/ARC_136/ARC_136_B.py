n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

D = dict()
for i in range(n):
    if A[i] not in D:
        D[A[i]] = 1
    else:
        D[A[i]] += 1
    if B[i] not in D:
        D[B[i]] = -1
    else:
        D[B[i]] -= 1

ans = True
for x in D:
    if D[x] != 0:
        ans = False
        break

if ans:
    if len(A) == len(set(A)):
        ca,cb = 0,0
        for i in range(n):
            for j in range(i+1,n):
                if A[i] > A[j]:
                    ca += 1
                if B[i] > B[j]:
                    cb += 1
        if (ca + cb) % 2 != 0:
            ans = False

if ans:
    print("Yes")
else:
    print("No")