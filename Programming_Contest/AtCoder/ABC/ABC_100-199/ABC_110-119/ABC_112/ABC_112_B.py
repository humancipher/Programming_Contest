#python Time_Limit_Exceeded.py
"""
入力フォーマット
N T
c_1 t_1
.
.
.
c_N t_N
N:帰宅経路数, T:帰宅制限時間
c_i:i番目の経路のコスト, t_i:i番目の経路の時間
出力：時間T以内に帰宅可能な最小コストの経路(不可能なら"TLE")
"""

line1 = list(map(int, input().split(" ")))
N = line1[0]
T = line1[1]
line2 = []
for i in range(N):
	line2.append(list(map(int, input().split(" "))))

min=1001 #1<=T<=1000
for i in range(N):
	if line2[i][1]<=T and min>line2[i][0]:
		min=line2[i][0]

if min<1001:
	print(min)
else:
	print("TLE")
