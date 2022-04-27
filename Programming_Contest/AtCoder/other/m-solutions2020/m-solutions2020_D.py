def solve(A,N):
    A.append(0)
    money,kabu = 1000,0
    ans = money
    pt = 0
    while pt < N:
        if A[pt] < A[pt+1]:
            ans = max(ans,money)
            kabu += (money // A[pt])
            money %= A[pt]
            pt += 1
            while pt < N:
                if A[pt] > A[pt+1]:
                    money += (A[pt] * kabu)
                    kabu = 0
                    ans = money
                    pt += 1
                    break
                else:
                    pt += 1
        else:
            pt += 1

    return ans

def main():
    N = int(input())
    A = list(map(int,input().split()))

    print(solve(A,N))

if __name__ == "__main__":
    main()
