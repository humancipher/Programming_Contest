from math import sqrt

N = 10**4

def divisor_sum(n):
    output = 0
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            output += i
            output += (n // i)
    if int(sqrt(n))**2 == n:
        output -= int(sqrt(n))
    output -= n
    return output

ans = 0
for i in range(1,N):
    pair = divisor_sum(i)
    if divisor_sum(pair) == i and pair != i:
        ans += i
print(ans)
