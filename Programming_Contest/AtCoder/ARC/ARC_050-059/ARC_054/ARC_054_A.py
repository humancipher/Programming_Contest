INF = 10**10

def main():
    import sys
    input = sys.stdin.readline
    l,x,y,s,d = map(int,input().split())
    if s == d:
        t = 0
    elif s < d:
        t1 = (d-s) / (y+x)
        if y > x:
            t2 = (l-(d-s)) / (y-x)
        else:
            t2 = INF
        t = min(t1,t2)
    else:
        t1 = (l-(s-d)) / (y+x)
        if y > x:
            t2 = (s-d) / (y-x)
        else:
            t2 = INF
        t = min(t1,t2)
    print(t)

if __name__ == "__main__":
    main()
