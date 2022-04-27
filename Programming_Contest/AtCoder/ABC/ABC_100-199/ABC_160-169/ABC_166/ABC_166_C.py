N,M = map(int,input().split())
H = list(map(int,input().split()))
AB = [list(map(int,input().split())) for _ in range(M)]

T = [1 for _ in range(N)]
for a,b in AB:
    if H[a-1] >= H[b-1]:
        T[b-1] = 0
    if H[a-1] <= H[b-1]:
        T[a-1] = 0

print(sum(T))
