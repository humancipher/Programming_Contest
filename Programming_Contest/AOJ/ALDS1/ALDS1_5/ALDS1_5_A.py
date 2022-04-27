from time import time

def bit_all(A,n):
    Ans = set()
    for i in range(2**n):
        kouho = 0
        for j in range(n):
            if i & 2**j:
                kouho += A[j]
        Ans.add(kouho)
    return Ans

def solve(A,n,M,q):
    S = bit_all(A,n)
    for i in range(q):
        if M[i] in S:
            print("yes")
        else:
            print("no")

def main():
    n = int(input())
    A = list(map(int,input().split()))
    q = int(input())
    M = list(map(int,input().split()))
    solve(A,n,M,q)

if __name__ == "__main__":
    main()
