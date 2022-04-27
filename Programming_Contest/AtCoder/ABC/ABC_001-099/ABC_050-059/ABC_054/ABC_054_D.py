INF = 1 << 60

def half(ABC,N):
    Ans = dict()
    for i in range(2**N):
        a,b,c = 0,0,0
        for j in range(N):
            if i & 2**j:
                a += ABC[j][0]
                b += ABC[j][1]
                c += ABC[j][2]
        if (a,b) in Ans:
            Ans[(a,b)] = min(Ans[(a,b)],c)
        else:
            Ans[(a,b)] = c
    return Ans

def solve(ABC,N,Ma,Mb):
    L,R = half(ABC[:N//2],N//2),half(ABC[N//2:],N-N//2)
    maxA,maxB = 0,0
    for i in range(N):
        maxA += ABC[i][0]
        maxB += ABC[i][1]
    Kouho = []
    x = 1
    while True:
        if maxA >= x*Ma and maxB >= x*Mb:
            Kouho.append((x*Ma,x*Mb))
            x += 1
        else:
            break
    ans = INF
    for a,b in L:
        for i in range(len(Kouho)):
            ma,mb = Kouho[i][0],Kouho[i][1]
            if (ma-a,mb-b) in R:
                ans = min(ans,L[(a,b)]+R[(ma-a,mb-b)])
    if ans != INF:
        return ans
    else:
        return -1

def main():
    N,Ma,Mb = map(int,input().split())
    ABC = [list(map(int,input().split())) for _ in range(N)]
    print(solve(ABC,N,Ma,Mb))

if __name__ == "__main__":
    main()

