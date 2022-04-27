def fib(k):
    F = [0 for _ in range(k+1)]
    F[0],F[1] = 1,2
    for i in range(2,k+1):
        F[i] = F[i-1] + F[i-2]

    return (F[k],F[k-1])

def main():
    K = int(input())

    f = fib(K)
    print(f[0],f[1])

if __name__ == "__main__":
    main()
