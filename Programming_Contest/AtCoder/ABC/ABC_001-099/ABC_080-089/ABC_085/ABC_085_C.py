def judge(N,Y):
    a,b,c = 10000,5000,1000
    if Y % c != 0 or Y < c or N*a < Y:
        return (-1,-1,-1)
    else:
        a,b,c,Y = a//1000,b//1000,c//1000,Y//1000
        for s in range(N+1):
            for t in range(N-s+1):
                u = N-s-t
                if a*s + b*t + c*u == Y:
                    return (s,t,u)
        return (-1,-1,-1)

def main():
    N,Y = map(int,input().split())

    ans = judge(N,Y)
    print(" ".join(map(str,ans)))

if __name__ == "__main__":
    main()
