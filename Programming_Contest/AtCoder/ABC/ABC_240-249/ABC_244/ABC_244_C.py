n = int(input())
Use = [True] * (2*n+2)
cnt = 0
while cnt < n+1:
    for i in range(1,2*n+2):
        if Use[i]:
            Use[i] = False
            print(i)
            break
    tmp = int(input())
    Use[tmp] = False
    cnt += 1
