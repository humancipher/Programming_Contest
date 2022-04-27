N = int(input())
xyh = [list(map(int,input().split())) for _ in range(N)]

"""
方針：0<=cx,cy<=100なのでcx,cyの特定は全数探索で間に合う
(cx,cy)があっていればh+(abs(cx-x)+abs(cy-y))=const
"""

xyh.sort(reverse=True,key = lambda x:x[2])

for cx in range(101):
	for cy in range(101):
		H = xyh[0][2] + (abs(cx-xyh[0][0]) + abs(cy-xyh[0][1]))
		correct_center = True
		for i in range(N):
			if max(H-(abs(cx-xyh[i][0]) + abs(cy-xyh[i][1])),0) != xyh[i][2]:
				correct_center = False
				break
		if correct_center:
			break
	if correct_center:
		break

print(cx,cy,H)
