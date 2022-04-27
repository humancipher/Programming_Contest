from math import sqrt

def eratos(n):
    P = [True] * (n+1)
    for i in range(2,int(sqrt(n))+1):
        if P[i]:
            for j in range(2,n//i+1):
                P[i*j] = False
    Ans = []
    for i in range(2,n+1):
        if P[i]:
            Ans.append(i)
    return Ans

def solve(a,b):
    P = eratos(int(sqrt(b))+1)
    D = [1] * (b-a+1)
    for p in P:
        for j in range(max(2,a//p),b//p+1):
            pt = p * j - a
            if pt < 0:
                continue
            if pt < len(D):
                D[pt] = 0
            else:
                break
    return sum(D)

def main():
    a,b = map(int,input().split())
    print(solve(a,b))

if __name__ == "__main__":
    main()
