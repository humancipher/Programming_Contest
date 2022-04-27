import math
N = int(input())
#(1,2,...,N)に対してP=(2,3,...,N,1)が最善

sum = (N-1)*N//2
#何故かsum = int(1/2*(N-1)*N)だとNによっては間違った計算をする
#//で割ると商(整数)を返すのに対して/で割ると浮動小数点数を返すのが原因か 
print(sum)