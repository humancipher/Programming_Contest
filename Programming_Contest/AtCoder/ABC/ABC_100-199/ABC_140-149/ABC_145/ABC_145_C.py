import itertools
import math

N = int(input())
C = [list(map(int,input().split())) for _ in range(N)]

def dist(x0,y0,x1,y1):
    return math.sqrt((x0-x1)**2+(y0-y1)**2)

Pt = list(itertools.permutations(range(N)))

distsum = 0
for i in range(len(Pt)):
    for j in range(N-1):
        distsum += dist(C[Pt[i][j]][0],C[Pt[i][j]][1],C[Pt[i][j+1]][0],C[Pt[i][j+1]][1])

print(distsum / len(Pt))
