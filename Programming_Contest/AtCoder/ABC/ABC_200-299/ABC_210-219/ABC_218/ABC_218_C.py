def fstjudge(S,T,n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if S[n+i][n+j] == "#":
                cnt += 1
            if T[i][j] == "#":
                cnt -= 1
    return cnt == 0

def rotation(T,n):
    A = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = T[j][n-1-i]
    return A

def judge(S,T,n,x,y):
    for i in range(n):
        for j in range(n):
            if S[i+x][j+y] != T[i][j]:
                return False
    return True

def main():
    n = int(input())
    S = [["." for _ in range(n)] + list(input()) + ["." for _ in range(n)] for _ in range(n)]
    Spad = [["." for _ in range(3*n)] for _ in range(n)]
    S = Spad + S + Spad
    T = [list(input()) for _ in range(n)]
    sx,sy = 4*n,4*n #Sの左上の#
    #SとTで左上の座標が合うやつだけ判定したい
    for i in range(n,2*n):
        for j in range(n,2*n):
            if S[i][j] == "#":
                sx,sy = min(sx,i),min(sy,j)
    ans = "No"
    if fstjudge(S,T,n):
        for _ in range(4):
            tx,ty = 4*n,4*n #Tの左上の#
            for i in range(n):
                for j in range(n):
                    if T[i][j] == "#":
                        tx,ty = min(tx,i),min(ty,j)
            if judge(S,T,n,sx-tx,sy-ty):
                ans = "Yes"
                break
            T = rotation(T,n)
    else:
        ans = "No"
    print(ans)

if __name__ == "__main__":
    main()
