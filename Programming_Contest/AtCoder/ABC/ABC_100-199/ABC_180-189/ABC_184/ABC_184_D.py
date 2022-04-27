A,B,C = map(int,input().split())

DP = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

DP[A][B][C] = 1

for a in range(A,101):
    for b in range(B,101):
        for c in range(C,101):
            if a-1 >= 0 and b < 100 and c < 100 and a+b+c-1 > 0:
                DP[a][b][c] += DP[a-1][b][c] * (a-1) / (a+b+c-1)
            if b-1 >= 0 and c < 100 and a < 100 and a+b+c-1 > 0:
                DP[a][b][c] += DP[a][b-1][c] * (b-1) / (a+b+c-1)
            if c-1 >= 0 and a < 100 and b < 100 and a+b+c-1 > 0:
                DP[a][b][c] += DP[a][b][c-1] * (c-1) / (a+b+c-1)

ans = 0
for a in range(A,101):
    for b in range(B,101):
        for c in range(C,101):
            S = [a,b,c]
            S.sort(reverse = True)
            if S[0] == 100 and S[1] < 100:
                ans += (a+b+c-A-B-C) * DP[a][b][c]

print(ans)
