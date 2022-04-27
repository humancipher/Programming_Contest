N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

Re = [False for _ in range(N)]
#Re[i]:i回目で勝った

def plus(t):
    if t == "r":
        return P
    elif t == "s":
        return R
    else:
        return S

ans = 0
for i in range(K):
    ans += plus(T[i])
    Re[i] = True

for i in range(K,N):
    if T[i] != T[i-K] or not Re[i-K]:
        ans += plus(T[i])
        Re[i] = True

print(ans)
