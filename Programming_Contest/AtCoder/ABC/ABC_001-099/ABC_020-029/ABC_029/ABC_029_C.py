from itertools import product

N = int(input())

P = "abc"
Ans = list(product(P,repeat = N))
for i in range(len(Ans)):
    ans = "".join(Ans[i])
    Ans[i] = ans

for i in range(len(Ans)):
    print(Ans[i])
