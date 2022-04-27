n = int(input())
T = list(map(int,input().split()))
ans = 0
for t in T:
    tmp = 2**t
    if tmp > ans:
        ans = tmp
    else:
        tmp2 = ans
        ans = 2**t
        b = t+1
        while ans <= tmp2:
            ans |= 2**b
            b += 1
        for i in reversed(range(t+1,b+1)):
            if ans - 2**i > tmp2:
                ans -= 2**i
print(ans)