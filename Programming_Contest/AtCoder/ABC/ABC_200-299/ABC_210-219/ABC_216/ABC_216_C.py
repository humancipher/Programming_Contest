n = int(input())
Ans = []
while n > 0:
    if n % 2 == 0:
        Ans.append("B")
        n //= 2
    else:
        Ans.append("A")
        n -= 1
for i in range(len(Ans)//2):
    Ans[i],Ans[len(Ans)-1-i] = Ans[len(Ans)-1-i],Ans[i]
print("".join(Ans))
