def time(x,p):
    return x + p / (2**(x/1.5))

def solve(p):
    left,right = 0,100
    while (right-left) > 10**(-10):
        #三分探索 凸関数の極値の近似値を求めるために使う
        a,b = left*2/3+right/3,left/3+right*2/3 #mid_left,mid_right
        if time(a,p) > time(b,p):
            left = a
        else:
            right = b
    return time(left,p)

def main():
    P = float(input())
    print(solve(P))

if __name__ == "__main__":
    main()
