N = int(input())
S = [input() for _ in range(N)]

voted = dict()
for i in range(N):
    if S[i] not in voted:
        voted[S[i]] = 1
    else:
        voted[S[i]] += 1

ans,max_vote = "",0
for v in voted:
    if voted[v] > max_vote:
        ans = v
        max_vote = voted[v]

print(ans)
