n = int(input())
D = set()
Ans = []
for i in range(n):
    S = input()
    if S not in D:
        D.add(S)
        Ans.append(i+1)
for i in range(len(Ans)):
    print(Ans[i])