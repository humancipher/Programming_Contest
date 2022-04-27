def comb(n): #C(n,k) mod 3のリスト
    T = [0 for _ in range(n+1)] #T[i]:iが3で割り切れる回数
    U = [1 for _ in range(n+1)] #P[i]:3**T[i]
    n3 = 3
    while n3 <= n:
        for i in range(1,n // n3 + 1):
            T[n3 * i] += 1
            U[n3 * i] *= 3
        n3 *= 3
    M = [(i // U[i]) % 3 for i in range(n+1)]
    M[0] = 1
    TR = [T[i] for i in range(n+1)] #Tの累積和
    for i in range(1,n+1):
        M[i] *= M[i-1]
        M[i] %= 3
        TR[i] += TR[i-1]
    CNK = []
    for k in range(n+1):
        if TR[n] > TR[k] + TR[n-k]:
            CNK.append(0)
        else:
            cnk = (M[n] * M[k] * M[n-k]) % 3
            CNK.append(cnk)
    return CNK

N = int(input())
C = list(input())

D = {"B":0,"W":1,"R":2}
E = {0:"B",1:"W",2:"R"}
for i in range(N):
    C[i] = D[C[i]]
CNK = comb(N-1)
ans = 0
for i in range(N):
    ans += CNK[i] * C[i]
    ans %= 3
if N % 2 == 0:
    ans *= -1
    ans %= 3
ans = E[ans]
print(ans)
