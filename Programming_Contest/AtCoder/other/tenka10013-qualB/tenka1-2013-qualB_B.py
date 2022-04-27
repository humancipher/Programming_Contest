q,l = map(int,input().split())
CMDS = [list(input().split()) for _ in range(q)]
stopped = False
stk = []
stk_len = 0

for i in range(q):
    CMD = CMDS[i]
    if CMD[0] == "Push":
        n,m = int(CMD[1]),int(CMD[2])
        if stk_len + n > l:
            print("FULL")
            stopped = True
            break
        else:
            stk.append([m,n])
            stk_len += n
    if CMD[0] == "Pop":
        n = int(CMD[1])
        if stk_len < n:
            print("EMPTY")
            stopped = True
            break
        else:
            while n > 0:
                [a,b] = stk.pop()
                if b > n:
                    stk.append([a,b-n])
                    stk_len -= n
                    n = 0
                else:
                    n -= b
                    stk_len -= b
    if CMD[0] == "Top":
        if stk_len <= 0:
            print("EMPTY")
            stopped = True
            break
        else:
            [a,b] = stk.pop()
            print(a)
            stk.append([a,b])
    if CMD[0] == "Size":
        print(stk_len)

if not stopped:
    print("SAFE")
