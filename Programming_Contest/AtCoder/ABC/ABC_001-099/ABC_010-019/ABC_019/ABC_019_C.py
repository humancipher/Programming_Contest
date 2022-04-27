def change(n):
    while n % 2 == 0:
        n //= 2
    return n

def main():
    N = int(input())
    A = list(map(int,input().split()))

    for i in range(N):
        A[i] = change(A[i])
    
    ans = len(set(A))
    print(ans)

if __name__ == "__main__":
    main()
