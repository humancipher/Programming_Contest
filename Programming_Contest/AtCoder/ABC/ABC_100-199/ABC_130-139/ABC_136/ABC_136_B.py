import math

N=int(input())

keta=0
while N>=math.pow(10,keta):
	keta += 1

count=0
if keta%2==1:
	count = N-int(math.pow(10,keta-1))+1
	keta -= 1
while keta>=2:
	count += 9*int(math.pow(10,keta-2))
	keta -= 2

print(count)