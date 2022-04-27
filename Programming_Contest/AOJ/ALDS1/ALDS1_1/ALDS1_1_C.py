import math

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

def PrimeJudge(a):
    if a == 2:
        return 1
    if a < 2 or a % 2 ==0:
        return 0
    i = 3
    while i <= int(math.sqrt(a)):
        if a % i == 0:
            return 0
        i += 2
    return 1

count = 0
for i in range(n):
    if PrimeJudge(A[i])==1:
        count += 1
print(count)
