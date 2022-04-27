def big_judge(R,N):
    tmp,n = 1,0
    while tmp <= 10**9 and n < N:
        tmp *= R
        if tmp > 10**9:
            return True
            break
        n += 1
    return False

def cal(A,R,N):
    if R == 1:
        if A > 10**9:
            return "large"
        else:
            return A
    else:
        if big_judge(R,N-1):
            return "large"
        else:
            p = pow(R,N-1)
            if A*p > 10**9:
                return "large"
            else:
                return A*p

def main():
    A,R,N = map(int,input().split())

    ans = cal(A,R,N)
    print(ans)

if __name__ == "__main__":
    main()
