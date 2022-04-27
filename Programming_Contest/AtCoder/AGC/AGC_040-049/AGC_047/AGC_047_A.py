from math import gcd

def Count_tf(a):
    two,five = 0,0
    while a % 2 == 0:
        two += 1
        a //= 2
    while a % 5 == 0:
        five += 1
        a //= 5
    return (two,five)

def kiyaku(a):
    a = int(a * 10**9)
    g = gcd(a,10**9)
    return (a//g,10**9//g)

def main():
    N = int(input())
    A = [float(input()) for _ in range(N)]

    B,C = [],[]
    for i in range(N):
        ki = kiyaku(A[i])
        B.append(ki[0]) #分子
        C.append(ki[1]) #分母

    D = {}
    ans = 0
    for i in range(N):
        ctfb,ctfc = Count_tf(B[i]),Count_tf(C[i])
        
        if (ctfb[0]-ctfc[0],ctfb[1]-ctfc[1]) in D:
            D[(ctfb[0]-ctfc[0],ctfb[1]-ctfc[1])] += 1
        else:
            D[(ctfb[0]-ctfc[0],ctfb[1]-ctfc[1])] = 1

        if ctfb[0]-ctfc[0] >= 0 and ctfb[1]-ctfc[1] >= 0:
            ans -= 1

    for d1 in D:
        for d2 in D:
            if d1[0] + d2[0] >= 0 and d1[1] + d2[1] >= 0:
                ans += D[d1] * D[d2]

    print(ans//2)

if __name__ == "__main__":
    main()
