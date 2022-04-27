n = int(input())
ST = [list(input().split()) for _ in range(n)]
ans = "No"
for a in range(n):
    for b in range(a+1,n):
        if ST[a][0] == ST[b][0] and ST[a][1] == ST[b][1]:
            ans = "Yes"
print(ans)
