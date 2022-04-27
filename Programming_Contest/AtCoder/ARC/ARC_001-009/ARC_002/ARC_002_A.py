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

y = int(input())

if judge(y):
    print("YES")
else:
    print("NO")
