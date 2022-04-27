n = int(input())
ST = [list(map(int,input().split())) for _ in range(n)]

ST.sort(key = lambda x:x[1])
Ans = [ST[0]]
for i in range(1,n):
    if Ans[-1][1] <= ST[i][0]:
        Ans.append(ST[i])
print(len(Ans))