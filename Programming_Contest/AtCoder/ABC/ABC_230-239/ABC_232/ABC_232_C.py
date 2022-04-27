from itertools import permutations

n,m = map(int,input().split())
AB,CD = set(),set()
for _ in range(m):
    a,b = map(int,input().split())
    AB.add((a-1,b-1))
    AB.add((b-1,a-1))
for _ in range(m):
    a,b = map(int,input().split())
    CD.add((a-1,b-1))
    CD.add((b-1,a-1))

P = list(permutations([i for i in range(n)]))

ans = "No"
for p in P:
    flag = True
    for a,b in AB:
        if (p[a],p[b]) not in CD:
            flag = False
            break
    if flag:
        ans = "Yes"
        break
print(ans)