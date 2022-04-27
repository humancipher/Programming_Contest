def solve(r,x,y):
    d2 = x**2 + y**2
    if r**2 > d2:
        return 2
    else:
        ans = 1
        while True:
            if (ans-1)**2 * r**2 < d2 <= ans**2 * r**2:
                return ans
            else:
                ans += 1

def main():
    r,x,y = map(int,input().split())
    print(solve(r,x,y))

if __name__ == "__main__":
    main()
