N = int(input())
S = input()

s = "b"
L,R = "",""
cnt = 0
ans = -1
if N % 2 != 0:
    while 1 + 2 * cnt < N:
        if cnt % 3 == 0:
            s = "a" + s + "c"
        elif cnt % 3 == 1:
            s = "c" + s + "a"
        else:
            s = "b" + s + "b"
        cnt += 1
    if S == s:
        ans = cnt

print(ans)
