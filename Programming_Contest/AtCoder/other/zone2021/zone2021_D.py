from collections import deque

def dec(C):
    rev = False
    T = deque()
    for i in range(len(C)):
        if C[i] == "R":
            rev = not rev
        else:
            if rev:
                T.appendleft(C[i])
            else:
                T.append(C[i])
    T = list(T)
    if rev:
        for i in range(len(T)//2):
            T[i],T[-1-i] = T[-1-i],T[i]
    Ans = []
    pt = 0
    while pt < len(T):
        if len(Ans) >= 1:
            if Ans[-1] == T[pt]:
                Ans.pop()
                pt += 1
            else:
                Ans.append(T[pt])
                pt += 1
        else:
            Ans.append(T[pt])
            pt += 1
    return "".join(Ans)

S = input()
print(dec(S))
