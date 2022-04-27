def main():
    N,K = map(int,input().split())

    A,AB = set(),{}
    for i in range(N):
        a,b = map(int,input().split())
        if a not in A:
            A.add(a)
            AB[a] = b
        else:
            AB[a] += b

    A = list(A)
    A.sort()

    for i in range(len(A)):
        K -= AB[A[i]]
        if K <= 0:
            ans = A[i]
            break

    print(ans)

if __name__ == "__main__":
    main()
