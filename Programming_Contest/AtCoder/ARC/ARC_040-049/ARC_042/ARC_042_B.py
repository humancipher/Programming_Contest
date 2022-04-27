from math import sqrt

def siki(x1,y1,x2,y2):
    #式をa*x+b*y+c=0としてreturn (a,b,c)
    #(x2-x1)*(y-y1)=(y2-y1)*(x-x1)
    #(y2-y1)*x+(x1-x2)*y+(x1*(y1-y2)+y1*(x2-x1))=0
    return (y2-y1 , x1-x2 , x1*(y1-y2)+y1*(x2-x1))

def dist(a,b,c,x0,y0):
    #直線ax+by+c=0と点(x0,y0)の距離
    return abs(a*x0+b*y0+c)/sqrt(a**2+b**2)

def main():
    sx,sy = map(int,input().split())
    N = int(input())
    xy = [list(map(int,input().split())) for _ in range(N)]

    ans = 101 #INF
    for i in range(N):
        x1,y1,x2,y2 = xy[i][0],xy[i][1],xy[(i+1)%N][0],xy[(i+1)%N][1]
        abc = siki(x1,y1,x2,y2)
        a,b,c = abc[0],abc[1],abc[2]
        d = dist(a,b,c,sx,sy)
        ans = min(ans,d)

    print(ans)

if __name__ =="__main__":
    main()
