N,K = map(int,input().split())

digit = 1
while N >= K**digit:
    digit += 1

print(digit)
