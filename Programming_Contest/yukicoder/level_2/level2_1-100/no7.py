from math import sqrt

def eratos(n):
    E = [True for _ in range(n+1)] #E[i]:iが素数かどうか
    E[0],E[1] = False,False
    for a in range(2,int(sqrt(n))+1):
        if E[a]:
            for i in range(2,n // a + 1):
                E[a * i] = False
    P = set()
    for a in range(n+1):
        if E[a]:
            P.add(a)
    return P

def solve(n):
    dp = [False for _ in range(n+1)] #dp[i]:iで先手番になったら先手が勝利かどうか
    dp[0],dp[1] = True,True
    P = eratos(n)
    for i in range(n+1):
        for p in P:
            if i-p >= 0:
                if not dp[i-p]:
                    dp[i] = True
    return dp[n]

def main():
    n = int(input())
    if solve(n):
        print("Win")
    else:
        print("Lose")

if __name__ == "__main__":
    main()
