from math import ceil

def judge(R,B,x,y,m): #m組の花束を作れるか
    # m0*x+m1 <= R
    # m0 + m1*y <= B
    # m0 + m1 == 1
    #を満たすm0が存在するなら条件にあう花束を作れる
    if (y*m-B) * (x-1) > (R-m) * (y-1):
        return False
    else:
        if (y*m-B)//(y-1) < (R-m)//(x-1) or (y*m-B)%(y-1) == 0 or (R-m)%(x-1) == 0:
            if ceil((y*m-B)/(y-1)) <= m and (R-m)//(x-1) >= 0: #0 <= m0,m1 <= m
                return True
            else:
                return False
        else:
            return False

def solve(R,B,x,y):
    left,right = 0,max(R,B)+1
    while right - left > 1:
        mid = (left+right)//2
        if judge(R,B,x,y,mid):
            left = mid
        else:
            right = mid
    return left

def main():
    R,B = map(int,input().split())
    x,y = map(int,input().split())
    print(solve(R,B,x,y))

if __name__ == "__main__":
    main()
