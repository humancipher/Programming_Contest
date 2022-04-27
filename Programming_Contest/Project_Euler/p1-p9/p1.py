N = 999

d3,d5,d15 = N // 3,N // 5,N // 15

def n_sum(n):
    return n*(n+1)//2

ans = 3*n_sum(d3)+5*n_sum(d5)-15*n_sum(d15)

print(ans)
