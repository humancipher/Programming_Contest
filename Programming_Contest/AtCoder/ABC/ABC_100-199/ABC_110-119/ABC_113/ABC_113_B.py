"""
入力フォーマット
N
T A
H_1 ... H_N

N:候補地点数
T:標準気温
A:所望の気温
H_i:地点iの高さ

高さxの地点の平均気温はT-x*0.06
"""

N = int(input())
line = input().rstrip().split(" ")
T = int(line[0])
A = int(line[1])
H = list(map(int, input().split(" ")))

min = 1000
min_i = 0
for i in range(N):
	if min > abs(A-(T-0.006*H[i])):
		min = abs(A-(T-0.006*H[i]))
		min_i = i+1


print(min_i)
