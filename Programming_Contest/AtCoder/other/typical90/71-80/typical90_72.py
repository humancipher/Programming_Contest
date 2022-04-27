def dfs(C,h,w,px,py,S,V,sx,sy):
    #V:移動方向、S:訪問済のマス
    ans = -1
    for (vx,vy) in V:
        if 0 <= px+vx < h and 0 <= py+vy < w:
            if C[px+vx][py+vy] == ".":
                if (px+vx,py+vy) in S:
                    if len(S) >= 3 and (px+vx,py+vy) == (sx,sy):
                        ans = max(ans,len(S))
                else:
                    ans = max(ans,dfs(C,h,w,px+vx,py+vy,S | set([(px+vx,py+vy)]),V,sx,sy))
    return ans

def main():
    h,w = map(int,input().split())
    C = [input() for _ in range(h)]
    
    V = [(0,1),(0,-1),(1,0),(-1,0)]
    ans = -1
    for i in range(h):
        for j in range(w):
            if C[i][j] == ".":
                ans = max(ans,dfs(C,h,w,i,j,set([(i,j)]),V,i,j))
    print(ans)

if __name__ == "__main__":
    main()
