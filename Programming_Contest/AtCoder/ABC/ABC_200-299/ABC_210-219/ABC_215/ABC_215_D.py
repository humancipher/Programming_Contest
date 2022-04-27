from math import sqrt

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))

    M = [True for _ in range(m+1)]
    for i in range(n):
        div = divisor(A[i])
        for d in div:
            if d <= m:
                if M[d]:
                    for j in range(m //d  + 1):
                        M[d*j] = False
    cnt,Ans = 0,[]
    for i in range(1,m+1):
        if M[i]:
            cnt += 1
            Ans.append(i)
    print(cnt)
    for i in range(len(Ans)):
        print(Ans[i])

def divisor(a):
    Ans = set()
    for i in range(1,int(sqrt(a))+1):
        if a % i == 0:
            Ans.add(i)
            Ans.add(a//i)
    Ans.discard(1)
    Ans = list(Ans)
    Ans.sort()
    return Ans

if __name__ == "__main__":
    main()
