INF = 10**20

def judge(a,b,n):
    return (a+b)*(a**2+b**2) >= n

def solve(n):
    limit = int(pow(n,1/3))+2
    ans = INF
    for a in range(limit):
        left,right = 0,limit
        while right-left > 1:
            mid = (left+right)//2
            if judge(a,mid,n):
                right = mid
            else:
                left = mid
        b = right
        ans = min(ans,(a+b)*(a**2+b**2))        
        if a >= b:
            break
    return ans

def main():
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(solve(n))

if __name__ == "__main__":
    main()
