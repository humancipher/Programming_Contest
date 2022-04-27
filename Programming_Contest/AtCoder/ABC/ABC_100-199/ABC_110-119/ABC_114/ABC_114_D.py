from bisect import bisect_left

def fact(n): #nの素因数分解
    x = n
    a = 2
    Ans = dict()
    while a**2 <= x and n > 1:
        if n % a == 0:
            Ans[a] = 1
            n //= a
            while n % a == 0:
                Ans[a] += 1
                n //= a
        a += 1
    if n > 1:
        Ans[n] = 1
    return Ans

def Fact(n): #n!の素因数分解
    Ans = dict()
    for i in range(2,n+1):
        Tmp = fact(i)
        for t in Tmp:
            if t in Ans:
                Ans[t] += Tmp[t]
            else:
                Ans[t] = Tmp[t]
    return Ans

def solve(n):
    A = Fact(n)
    P = []
    for a in A:
        P.append(A[a]+1)
    P.sort()
    ans = 0
    ans += len(P) - bisect_left(P,75) #75個以上のやつを1個選ぶパターン
    ans += (len(P) - bisect_left(P,25)) * (len(P) - bisect_left(P,3) - 1) #25個以上のやつ1個と3以上のやつを1個選ぶパターン
    ans += (len(P) - bisect_left(P,15)) * (len(P) - bisect_left(P,5) - 1) #15以上のやつ1個と3以上のやつを1個選ぶパターン
    ans += (len(P) - bisect_left(P,5)) * (len(P) - bisect_left(P,5) - 1) * (len(P) - bisect_left(P,3) - 2) // 2 #5以上のやつを2個と3以上のやつを1個選ぶパターン
    return ans

def main():
    N = int(input())
    print(solve(N))

if __name__ == "__main__":
    main()
