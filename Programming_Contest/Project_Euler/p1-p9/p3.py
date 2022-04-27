N = 600851475143

def fact(n):
    P = []
    a = 2
    while n > 1:
        if n % a == 0:
            P.append(a)
            while n % a == 0:
                n //= a
        a += 1
    return P

ans = fact(N)
print(ans[len(ans)-1])
