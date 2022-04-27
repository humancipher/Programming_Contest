def eat(A,x):
    n = len(A)
    pt = 1
    output = 0
    while pt < n:
        if A[pt-1] + A[pt] > x:
            tmp = A[pt]
            A[pt] = max(0,x-A[pt-1])
            output += (tmp-A[pt])
        pt += 1
    if A[0] + A[1] > x:
        tmp = A[0]
        A[0] = max(0,x-A[1])
        output += (tmp-A[0])
    return output

def main():
    N,x = map(int,input().split())
    a = list(map(int,input().split()))

    ans = eat(a,x)

    print(ans)

if __name__ == "__main__":
    main()
