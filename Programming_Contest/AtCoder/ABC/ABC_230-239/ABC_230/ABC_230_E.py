n = int(input())

ans = 0
d = 1
while d <= n:
    q = n // d
    d_max = n // q
    ans += q*(d_max-d+1)
    d = d_max+1

print(ans)
