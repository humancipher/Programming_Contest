S0 = input()
S1 = input()

ans = "YES"
for i in range(3):
    if S0[i] != S1[2-i]:
        ans ="NO"
        break

print(ans)
