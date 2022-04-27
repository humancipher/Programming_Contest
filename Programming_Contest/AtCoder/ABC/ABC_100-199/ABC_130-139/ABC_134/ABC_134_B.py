import math

line = list(map(int, input().split(" ")))
N = line[0]
D = line[1]

bord = math.ceil(N/(2*D+1))

print(bord)
