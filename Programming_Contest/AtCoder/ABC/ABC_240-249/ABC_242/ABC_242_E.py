mod = 998244353
limit = 10**6
P26 = [1] * (limit+1)
for i in range(limit):
    P26[i+1] *= (P26[i] * 26)
    P26[i+1] %= mod

def mirror(S,n):
    T = [S[i] for i in range(n)]
    for i in range((n+1)//2):
        T[n-1-i] = S[i]
    return T <= S

def solve(S,n):
    ans = 0
    for i in range((n+1)//2):
        tmp = ((ord(S[i])-ord("A")) * P26[(n+1)//2-i-1]) % mod
        ans += tmp
        ans %= mod
    if mirror(S,n):
        ans += 1
        ans %= mod
    return ans

def main():
    t = int(input())
    Ans = list()
    for _ in range(t):
        n = int(input())
        S = list(input())
        Ans.append(solve(S,n))
    for i in range(t):
        print(Ans[i])

if __name__ == "__main__":
    main()
