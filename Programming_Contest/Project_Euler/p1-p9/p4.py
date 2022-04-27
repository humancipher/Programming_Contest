def judge(N):
    #6桁の回文になっているかどうか
    N = str(N)
    if len(N) != 6:
        return False
    else:
        for i in range(3):
            if N[i] != N[5-i]:
                return False
        return True

ans = 0
a = 110
while a < 1000:
    for b in range(100,999):
        if judge(a*b):
            ans = max(ans,a*b)
    a += 11

print(ans)
