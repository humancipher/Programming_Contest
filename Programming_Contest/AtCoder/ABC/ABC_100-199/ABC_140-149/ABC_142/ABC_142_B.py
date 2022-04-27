N, K = input().split()
H = [int(x) for x in input().split()]

cnt = 0
for i in range(int(N)):
    if H[i] >= int(K):
        cnt += 1
print(cnt)
