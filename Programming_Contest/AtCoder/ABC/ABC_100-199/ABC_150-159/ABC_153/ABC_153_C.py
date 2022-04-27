N,K = map(int,input().split())
H = list(map(int,input().split()))

H = sorted(H)
sum = 0
for i in range(N-K):
    sum += H[i]

print(sum)
