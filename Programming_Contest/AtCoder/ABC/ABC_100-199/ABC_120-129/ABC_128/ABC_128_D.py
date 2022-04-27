INF = 10**10

def solve(V,n,k,use,drop):
    if use > n or use < drop or use + drop > k:
        return -INF
    else:
        ans = -INF
        for i in range(use+1):
            A = V[:i] + V[len(V)-use+i:]
            A.sort(reverse = True)

            tmp = sum(A)
            cnt = 0
            while len(A) > 0 and cnt < drop:
                if A[len(A)-1] < 0:
                    tmp -= A[len(A)-1]
                    A.pop()
                    cnt += 1
                else:
                    break
            ans = max(ans,tmp)
        return ans

def main():
    n,k = map(int,input().split())
    V = list(map(int,input().split()))
    ans = 0
    for i in range(n+1):
        for j in range(k+1):
            tmp = solve(V,n,k,i,j)
            ans = max(ans,tmp)
    print(ans)

if __name__ == "__main__":
    main()
