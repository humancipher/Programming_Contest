S = input()
T = "oxx"*10**5
ans = "No"
for i in range(len(T)-len(S)):
    if S == T[i:i+len(S)]:
        ans = "Yes"
        break
print(ans)