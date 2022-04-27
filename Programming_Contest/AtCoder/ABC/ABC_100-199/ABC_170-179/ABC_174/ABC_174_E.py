def solve(A,N,K):
    ans_max,ans_min = max(A),1

    while True:
        if cutable(A,N,K,(ans_max+ans_min)//2):
            if ans_max > (ans_max+ans_min)//2:
                ans_max = (ans_max+ans_min)//2
            else:
                return ans_max
        else:
            if ans_min < (ans_max+ans_min)//2:
                ans_min = (ans_max+ans_min)//2
            else:
                return ans_max

def cutable(A,N,K,div):
    #K回までの切断で全部を長さdiv以下にできるかどうか
    cnt = 0
    for i in range(N):
        cnt += A[i]//div
        if A[i] % div == 0:
            cnt -= 1
        if cnt > K:
            return False

    return True

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    ans = solve(A,N,K)
    print(ans)

if __name__ == "__main__":
    main()
