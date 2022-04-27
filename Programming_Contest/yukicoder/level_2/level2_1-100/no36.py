from math import sqrt

n = int(input())

div = 2
fact = list()
while div < int(sqrt(n))+1 and n > 1:
    if n % div == 0:
        while n % div == 0:
            fact.append(div)
            n //= div
    div += 1
if n > 1:
    fact.append(n)

if len(fact) >= 3:
    print("YES")
else:
    print("NO")
