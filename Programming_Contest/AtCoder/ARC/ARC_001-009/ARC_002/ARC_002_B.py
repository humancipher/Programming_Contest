def judge(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def next(y,m,d):
    Month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if judge(y):
        Month[1] = 29

    while y % (m * d) != 0:
        if m == 12 and d == 31:
            y += 1
            m,d = 1,1
        elif Month[m-1] == d:
            m += 1
            d = 1
        else:
            d += 1

    y,m,d = str(y),str(m),str(d)
    if len(m) == 1:
        m = "0" + m
    if len(d) == 1:
        d = "0" + d
    return y + "/" + m + "/" + d

y,m,d =map(int,input().split("/"))

print(next(y,m,d))
