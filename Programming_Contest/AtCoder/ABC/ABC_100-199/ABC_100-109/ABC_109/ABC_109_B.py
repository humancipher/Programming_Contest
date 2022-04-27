N = int(input())
W = [input() for _ in range(N)]

S = set([W[0]])

ans = "Yes"
for i in range(1,N):
    if W[i-1][len(W[i-1])-1] != W[i][0] or W[i] in S:
        ans = "No"
        break
    else:
        S.add(W[i])

print(ans)
