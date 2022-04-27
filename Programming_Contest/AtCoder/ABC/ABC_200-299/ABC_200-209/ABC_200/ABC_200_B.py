def solve(n,k):
    if k == 0:
        return n
    else:
        if n % 200 == 0:
            n //= 200
        else:
            n = n * 1000 + 200
        return solve(n,k-1)

n,k = map(int,input().split())
print(solve(n, k))
