n,m = map(int,input().split())
S = list(input().split())
T = list(input().split())
ps,pt = 0,0
Ans = []
while pt < m:
    if S[ps] == T[pt]:
        Ans.append("Yes")
        ps += 1
        pt += 1
    else:
        Ans.append("No")
        ps += 1
for i in range(n):
    print(Ans[i])