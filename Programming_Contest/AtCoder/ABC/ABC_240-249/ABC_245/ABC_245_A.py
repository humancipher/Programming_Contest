a,b,c,d = map(int,input().split())
if a != c:
    if a < c:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if b <= d:
        print("Takahashi")
    else:
        print("Aoki")