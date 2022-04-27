from math import sin,cos,pi

def solve(x0,y0,X,Y,N):
    ox,oy = (x0+X)/2,(y0+Y)/2
    s0,t0 = x0-ox,y0-oy
    s1 = cos(pi/(N/2))*s0 - sin(pi/(N/2))*t0
    t1 = sin(pi/(N/2))*s0 + cos(pi/(N/2))*t0
    s1 += ox
    t1 += oy
    return str(s1) + " " + str(t1)

def main():
    N = int(input())
    x0,y0 = map(int,input().split())
    X,Y = map(int,input().split())
    
    print(solve(x0,y0,X,Y,N))

if __name__ == "__main__":
    main()
