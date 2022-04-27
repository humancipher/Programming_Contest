from math import sqrt

def eratos(n):
    P = [True] * (n+1)
    P[0],P[1] = False,False
    for i in range(int(sqrt(n))+1):
        if P[i]:
            for j in range(2,n//i+1):
                P[i*j] = False
    Ans = []
    for i in range(n+1):
        if P[i]:
            Ans.append(i)
    return Ans

def main():
    n = int(input())
    P = eratos(55555)
    Ans = []
    for i in range(len(P)):
        if P[i] % 5 == 1:
            Ans.append(P[i])
        if len(Ans) == n:
            break
    print(" ".join(map(str,Ans)))

if __name__ == "__main__":
    main()
