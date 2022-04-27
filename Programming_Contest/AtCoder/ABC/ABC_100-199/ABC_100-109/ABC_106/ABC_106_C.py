S = input()
K = int(input())

ans,pt = "1",0
for i in range(len(S)):
    if S[i] != "1":
        ans,pt = S[i],i
        break

if pt < K:
    print(ans)
else:
    print(1)
