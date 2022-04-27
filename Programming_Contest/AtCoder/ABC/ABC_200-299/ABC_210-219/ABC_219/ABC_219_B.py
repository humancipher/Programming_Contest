S = [input() for _ in range(3)]
T = list(input())
Ans = []
for i in range(len(T)):
    t = int(T[i])-1
    Ans.append(S[t])
print("".join(Ans))