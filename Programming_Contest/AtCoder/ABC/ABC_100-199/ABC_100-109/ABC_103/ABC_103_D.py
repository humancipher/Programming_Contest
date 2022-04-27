n,m = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(m)]
AB.sort(key = lambda x:x[1])

Ans = [AB[0]]
for i in range(1,m):
    if Ans[-1][1] <= AB[i][0]:
        Ans.append(AB[i])
print(len(Ans))
