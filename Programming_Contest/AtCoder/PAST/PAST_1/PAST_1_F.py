def S_split(S):
    output,PT = [],[]
    for i in range(len(S)):
        if 65 <= ord(S[i]) and ord(S[i]) <= 90:
            PT.append(i)
    pt = 0
    while pt < len(PT):
        output.append(S[PT[pt]:PT[pt+1]+1])
        pt += 2
    return output

def small(S):
    S = list(S)
    for i in range(len(S)):
        if 65 <= ord(S[i]) and ord(S[i]) <= 90:
            S[i] = chr(ord(S[i])+32)
    S = "".join(S)
    return S

S = input()

S = S_split(S)
S_ = []
for i in range(len(S)):
    S_.append(small(S[i]))

T = [(S[i],S_[i]) for i in range(len(S))]

T.sort(key = lambda x:x[1])

ans = [T[i][0] for i in range(len(T))]
ans = "".join(ans)
print(ans)
