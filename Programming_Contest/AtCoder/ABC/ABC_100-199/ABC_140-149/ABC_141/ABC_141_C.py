N, K, Q = map(int, input().split())
A = []
for i in range(Q):
    A.append(int(input()))

Ap = []
for i in range(N):
    Ap.append(0)

for i in range(Q):
    Ap[A[i]-1] += 1

for i in range(N):
    if K - (Q - Ap[i]) > 0:
        print('Yes')
        #print(K - (Q - Ap[i]))
    else:
        print('No')
        #print(K - (Q - Ap[i]))
