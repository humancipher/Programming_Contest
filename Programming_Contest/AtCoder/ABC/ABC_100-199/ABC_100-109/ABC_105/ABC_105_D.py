n,m = map(int,input().split())
A = list(map(int,input().split()))
A = [0] + A
Amari = dict() #Amari[i]:余りがiになる区間の取り方のパターン数
Amari[0] = 1
for i in range(n):
    A[i+1] += A[i]
    A[i+1] %= m
    if A[i+1] in Amari:
        Amari[A[i+1]] += 1
    else:
        Amari[A[i+1]] = 1
ans = 0
for r in Amari:
    ans += Amari[r]*(Amari[r]-1)//2
print(ans)