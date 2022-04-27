INF = 2 * 10**14

def judge(H,S,N,limit):
    Buf = [((limit - H[i]) // S[i]) for i in range(N)]
    Buf.sort()
    for i in range(N):
        if Buf[i] < i:
            return False
    return True

def solve(H,S,N):
    left,right = -1,INF
    while right - left > 1:
        mid = (left + right) // 2
        if judge(H,S,N,mid):
            right = mid
        else:
            left = mid
    return right

def main():
    N = int(input())
    HS = [list(map(int,input().split())) for _ in range(N)]
    H,S = [HS[i][0] for i in range(N)],[HS[i][1] for i in range(N)]

    print(solve(H,S,N))

if __name__ == "__main__":
    main()
