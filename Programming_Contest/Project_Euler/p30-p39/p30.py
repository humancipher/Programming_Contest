def judge(n):
    sum = 0
    for i in range(len(str(n))):
        sum += pow(int(str(n)[i]),5)
    if n == sum:
        return True
    else:
        return False

#6*9**5=354294
#7*9**5=413343
#よって各桁の5乗の和と元の数が一致する可能性があるのは6桁までで
#354294まで
N = 354294

ans = 0
for i in range(2,N+1):
    if judge(i):
        ans += i
print(ans)
