from math import sin,pi

def f(a,b,c,t):
    return a*t + b*sin(c*t*pi)

def b_search(a,b,c,tl,tr):
    while abs(f(a,b,c,tl)-f(a,b,c,tr)) > 10**(-7): #f(a,b,c,tl) <= 100 < f(a,b,c,tr)
        tm = (tl+tr)/2
        if f(a,b,c,tm) > 100:
            tr = tm
        else:
            tl = tm
    return tl

def main():
    a,b,c = map(int,input().split())
    ans = b_search(a,b,c,0,1000)
    print(ans)

if __name__ == "__main__":
    main()
