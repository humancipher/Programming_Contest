def diff(a,b):
    output = 0
    for i in range(N):
        if a[i] != b[i]:
            output += 1
    return output

S = input()
N = len(S)

S1,S2 = "",""
for i in range(N):
    if i % 2 == 0:
        S1 += "0"
        S2 += "1"
    else:
        S1 += "1"
        S2 += "0"

ans = min(diff(S,S1),diff(S,S2))
print(ans)
