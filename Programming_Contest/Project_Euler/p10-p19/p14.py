#pypyじゃないと非常に重い
N = 10**6

def collatz(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n+1
        count += 1
    return count

ans,max_len = 0,0
for i in range(1,N):
    if collatz(i) > max_len:
        ans,max_len = i,collatz(i)
print(ans)
