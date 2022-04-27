#pow(3,10)=59049なら全部考えても間に合いそう

def Bn(n,k,Digit):
    #10進数nをDigit桁k進数に変換
    output = ""
    digit = 1
    while n >= k**digit:
        digit += 1
    Digit -= digit
    if Digit > 0:
        for i in range(Digit):
            output += "0"
    while digit > 0:
        output += str(n//k**(digit-1))
        n %= k**(digit-1)
        digit -= 1
    return output

def score(a,A):
    output = 0
    for a1 in A:
        for a2 in A:
            if a1 < a2:
                output += a[a1-1][a2-1-a1]
    return output

N = int(input())
a = [list(map(int,input().split())) for _ in range(N-1)]
INF = 45*10**6+1

#a[i][j]が全部負だったりするとどう分けても不幸にしかない
ans = -INF
for i in range(pow(3,N)):
    g = Bn(i,3,N)
    A,B,C = [],[],[]
    for j in range(len(g)):
        if g[j] == "0":
            A.append(int(j+1))
        elif g[j] == "1":
            B.append(int(j+1))
        else:
            C.append(int(j+1))
    tmp = score(a,A) + score(a,B) + score(a,C)
    ans = max(tmp,ans)

print(ans)
