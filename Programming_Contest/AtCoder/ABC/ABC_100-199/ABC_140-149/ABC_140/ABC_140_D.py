n,k = map(int,input().split())
S = input()

S = "R" + S + "L"

ans = 0
for i in range(1,n+1):
    if S[i] == "L":
        if S[i-1] == "L":
            ans += 1
    if S[i] == "R":
        if S[i+1] == "R":
            ans += 1

ans += 2 * k
ans = min(ans,n-1)
print(ans)
