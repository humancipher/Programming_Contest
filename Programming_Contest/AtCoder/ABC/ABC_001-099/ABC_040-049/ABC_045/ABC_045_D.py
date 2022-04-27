def main():
    import sys
    input = sys.stdin.readline
    h,w,n = map(int,input().split())
    V = []
    D = dict() #D[(i,j)]:マス(i,j)周囲での塗りつぶし数
    Ans = [0] * 10
    Ans[0] = (h-2)*(w-2)
    for i in range(-1,2):
        for j in range(-1,2):
            V.append((i,j))
    for _ in range(n):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        for dx,dy in V:
            if 1 <= a+dx and a+dx <= h-2 and 1 <= b+dy and b+dy <= w-2:
                if (a+dx,b+dy) in D:
                    D[(a+dx,b+dy)] += 1
                else:
                    D[(a+dx,b+dy)] = 1
                    Ans[0] -= 1
    for x,y in D:
        Ans[D[(x,y)]] += 1
    for i in range(10):
        print(Ans[i])

if __name__ == "__main__":
    main()
