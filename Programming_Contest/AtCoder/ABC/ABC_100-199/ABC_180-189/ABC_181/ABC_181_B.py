def sigma(x):
    return x*(x+1)//2

ans = 0
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    ans += sigma(b) - sigma(a-1)
print(ans)
