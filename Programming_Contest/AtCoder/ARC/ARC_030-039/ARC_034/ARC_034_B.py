def digitsum(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

n = int(input())
Ans = []
for i in reversed(range(1,min(9*18,n)+1)):
    x = n-i
    if x+digitsum(x) == n:
        Ans.append(x)    
print(len(Ans))
for i in range(len(Ans)):
    print(Ans[i])