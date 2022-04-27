#python ABC_130_C.py

line = list(map(int, input().split(" ")))

W = line[0]
H = line[1]
x = line[2]
y = line[3]

S = W*H/2

if x==W/2 and y==H/2:
	flag=1
else:
	flag=0

print(S,flag)
