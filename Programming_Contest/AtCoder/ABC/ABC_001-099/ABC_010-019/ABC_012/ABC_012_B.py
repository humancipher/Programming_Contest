def pad(n):
    if len(str(n)) == 1:
        return "0"+str(n)
    else:
        return str(n)

n = int(input())
h = n // 3600
n %= 3600
m = n // 60
s = n - m * 60
print(pad(h)+":"+pad(m)+":"+pad(s))
