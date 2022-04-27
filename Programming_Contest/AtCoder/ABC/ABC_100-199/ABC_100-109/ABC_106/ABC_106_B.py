from math import sqrt

N = int(input())

def div_count(n):
    count = 0
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            count += 2
    if n == int(sqrt(n))**2:
        count -= 1
    return count

ans = 0
for i in range(1,N+1):
    if div_count(i) == 8 and i % 2 != 0:
        ans += 1

print(ans)
