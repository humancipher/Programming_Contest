from math import sqrt

def dist_sq(x0,y0,x1,y1):
    return (x0-x1)**2+(y0-y1)**2

def main():
    N = int(input())
    xy = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(dist_sq(xy[i][0],xy[i][1],xy[j][0],xy[j][1]),ans)

    print(sqrt(ans))

if __name__ == "__main__":
    main()
