def cal(A,N):
    OP = []
    for i in range(N):
        count,pt = 1,i+1
        while A[pt-1] != i+1:
            pt = A[pt-1]
            count += 1
        OP.append(count)

    return OP

def main():
    N = int(input())
    A = list(map(int,input().split()))

    ans = cal(A,N)
    ans = " ".join(map(str,ans))
    print(ans)

if __name__ == "__main__":
    main()
