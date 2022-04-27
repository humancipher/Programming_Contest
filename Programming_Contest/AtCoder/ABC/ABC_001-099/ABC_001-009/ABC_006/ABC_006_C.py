def cal(N,M):
    adult,old,baby = 0,0,0
    if N * 2 > M or N * 4 < M:
        adult,old,baby = -1,-1,-1
    elif N * 3 == M:
        adult,old,baby = 0,N,0
    elif N * 3 > M:
        t = N * 3 - M
        adult,old,baby = t,N-t,0
    else:
        t = M - N * 3
        adult,old,baby = 0,N-t,t
    return (adult,old,baby)

def main():
    N,M = map(int,input().split())
    ans = cal(N,M)
    print(" ".join(map(str,ans)))

if __name__ == "__main__":
    main()
