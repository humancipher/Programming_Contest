from math import sqrt

N = 500
"""
a_n = n*(n+1)//2
"""
def div_count(n):
    count = 0
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            count += 2
    if int(sqrt(n))**2 == n:
        count -= 1
    return count

x = 1
while div_count(x*(x+1)//2) <= N:
    x += 1

print(x*(x+1)//2)
