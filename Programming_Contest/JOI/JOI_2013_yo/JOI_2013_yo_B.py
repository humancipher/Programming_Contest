N = int(input())
ABC = [list(map(int,input().split())) for _ in range(N)]

P = [0 for _ in range(N)]

for i in range(3):
    for j in range(N):
        plus = ABC[j][i]
        for k in range(N):
            if ABC[j][i] == ABC[k][i] and j != k:
                plus = 0
                break
        P[j] += plus

for j in range(N):
    print(P[j])
