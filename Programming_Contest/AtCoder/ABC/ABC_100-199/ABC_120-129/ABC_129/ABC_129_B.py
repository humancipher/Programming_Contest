N = int(input())
W = list(map(int,input().split()))
INF = 10**4+1

for i in range(N-1):
    W[i+1] += W[i]

diff = INF
for i in range(N):
    diff = min(diff,abs(W[i]-(W[N-1]-W[i])))

print(diff)
