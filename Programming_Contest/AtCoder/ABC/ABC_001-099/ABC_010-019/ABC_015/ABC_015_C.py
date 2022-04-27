def solve(T,N,K,depth,xor):
    if depth == N:
        if xor == 0:
            return 1
        else:
            return 0
    else:
        ans = sum([solve(T,N,K,depth+1,xor ^ T[depth][k]) for k in range(K)])
        return ans

def main():
    N,K = map(int,input().split())
    T = [list(map(int,input().split())) for _ in range(N)]

    ans = solve(T,N,K,0,0)
    if ans == 0:
        print("Nothing")
    else:
        print("Found")

if __name__ == "__main__":
    main()
