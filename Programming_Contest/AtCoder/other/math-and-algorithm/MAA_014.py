from math import sqrt

n = int(input())
n0 = n
Ans = []
for i in range(2,int(sqrt(n0))+1):
    while n % i == 0:
        Ans.append(i)
        n //= i
if n != 1:
    Ans.append(n)
print(" ".join(map(str,Ans)))