N,K = map(int,input().split())
P = list(map(int,input().split()))

Q = [(P[i]+1)/2 for i in range(N)]

max,tmp = sum(Q[0:K]),sum(Q[0:K])
for i in range(N-K):
    tmp = tmp + Q[K+i] - Q[i]
    if max < tmp:
        max = tmp

print(max)
