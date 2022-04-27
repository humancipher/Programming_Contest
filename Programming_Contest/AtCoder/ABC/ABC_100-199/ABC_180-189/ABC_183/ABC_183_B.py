sx,sy,gx,gy = map(int,input().split())

ans = gx + gy * (sx-gx) / (sy+gy)
print(ans)
