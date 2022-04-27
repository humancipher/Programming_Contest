o = list(input())
e = list(input())

Ans = list()
for i in range(len(o)+len(e)):
    if i % 2 == 0:
        Ans.append(o[i//2])
    else:
        Ans.append(e[(i-1)//2])
print("".join(Ans))