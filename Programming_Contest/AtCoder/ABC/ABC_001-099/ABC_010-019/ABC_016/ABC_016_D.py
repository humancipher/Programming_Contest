def cross_judge(A,B,C,D):
    #線分ABと線分CDがが交差するかの判定
    xa,ya,xb,yb,xc,yc,xd,yd = A[0],A[1],B[0],B[1],C[0],C[1],D[0],D[1]
    s = (ya - yb) * xc + (xb - xa) * yc + xa * yb - xb * ya
    t = (ya - yb) * xd + (xb - xa) * yd + xa * yb - xb * ya
    u = (yc - yd) * xa + (xd - xc) * ya + xc * yd - xd * yc
    v = (yc - yd) * xb + (xd - xc) * yb + xc * yd - xd * yc
    if s * t < 0 and u * v < 0: #s * t のみの判定だとCDが直線扱い
        return True
    else:
        return False

def main():
    ax,ay,bx,by = map(int,input().split())
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    XY.append(XY[0])
    coll_count = 0
    for i in range(N):
        if cross_judge([ax,ay],[bx,by],XY[i],XY[i+1]):
            coll_count += 1
  
    print(coll_count // 2 + 1)

if __name__ == "__main__":
    main()
