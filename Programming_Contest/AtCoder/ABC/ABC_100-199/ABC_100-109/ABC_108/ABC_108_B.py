x1,y1,x2,y2 = map(int,input().split())

xy = [[x1,y1],[x2,y2]]

vec = [x2-x1,y2-y1]

A = [[0,-1],[1,0]]

for i in range(2):
    vec[0],vec[1] = A[0][0]*vec[0]+A[0][1]*vec[1],A[1][0]*vec[0]+A[1][1]*vec[1]
    xy.append([xy[-1][0]+vec[0],xy[-1][1]+vec[1]])

ans = ""
for i in range(2,4):
    ans += " ".join(map(str,xy[i]))
    ans += " "

print(ans[:-1])
