n,a,b = map(int,input().split())

M = 10**9+7

def pow(x,n,M):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow((x % M)**2, n // 2, M)
    if n % 2 == 1:
        return (x % M) * pow((x % M)**2, n // 2, M)

def inv(x,M): #法Mでのxの逆元,Mは素数
    return pow(x,M-2,M) % M

#2**n - 1 - C(n,a) - C(n,b)
Cna_nume,Cna_deno,Cnb_nume,Cnb_deno = 1,1,1,1
for i in range(1,a+1):
    Cna_nume *= (n-i+1)
    Cna_nume %= M
    #まとめてCna_nume *= (n-i+1)%Mとかすると重くなるようだ
    Cna_deno *= i
    Cna_deno %= M
for i in range(1,b+1):
    Cnb_nume *= (n-i+1)
    Cnb_nume %= M
    Cnb_deno *= i
    Cnb_deno %= M
Cna = (Cna_nume * inv(Cna_deno,M)) % M
Cnb = (Cnb_nume * inv(Cnb_deno,M)) % M

print((pow(2,n,M) - 1 - Cna - Cnb) % M)
