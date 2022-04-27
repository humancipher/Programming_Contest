from math import pi,sqrt,sin,cos

def main():
    A,B,H,M = map(int,input().split())

    a,b = 2*pi*(H/12+M/(60*12)),2*pi*(M/60)


    ans = sqrt(A**2 + B**2 - 2*A*B*cos(a-b))
    print(ans)

if __name__ == "__main__":
    main()
