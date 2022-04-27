N = int(input())
P = list(map(int,input().split()))

ans = 0
P_subset = set()
for i in range(N):
    P_subset.add(P[i])
    if ans not in P_subset:
        print(ans)
    else:
        while ans in P_subset:
            ans += 1
        print(ans)
