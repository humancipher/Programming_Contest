n = int(input())
S = input()
S = S +"_"
bef = ""
cnt = 1
ans = 0
for i in range(n+1):
    if bef != S[i]:
        bef = S[i]
        ans += (cnt*(cnt-1))//2
        cnt = 1
    else:
        cnt += 1
print(ans)
