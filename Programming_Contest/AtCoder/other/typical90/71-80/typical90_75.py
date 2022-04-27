from math import sqrt

def fact(n):
    cnt = 0
    for i in range(2,int(sqrt(n))+2):
        while n % i == 0:
            n //= i
            cnt += 1
    if n > 1:
        cnt += 1
    return cnt

n = int(input())
fcnt = fact(n)
ans = 0
while fcnt > 1:
    fcnt = (fcnt+1)//2
    ans += 1
print(ans)
