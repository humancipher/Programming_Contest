from math import sqrt

def fact(n):
    Ans = set()
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            Ans.add(i)
            Ans.add(n // i)
    return Ans

def main():
    n = int(input())
    Ans = fact(n-1) #n = n-kだけで1になるやつ
    Ans.discard(1)
    F = fact(n)
    F.discard(1)
    for k in F:
        m = n
        while m % k == 0:
            m //= k
        if m % k == 1:
            Ans.add(k)
    print(len(Ans))

if __name__ == "__main__":
    main()
