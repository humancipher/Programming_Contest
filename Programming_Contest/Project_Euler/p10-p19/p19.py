Month = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(12):
    Month[i] %= 7

def leap(year):
    if year % 4 == 0:
        if year % 400 != 0 and year % 100 == 0:
            return 0
        else:
            return 1
    else:
        return 0

#日曜:dw = 0, 月曜:dw = 1,...,土曜:dw = 6
dw = 1
dw = (dw + 365 + leap(1900)) % 7
ans = 0
if dw == 0:
    ans += 1

for i in range(1901,2001):
    for j in range(12):
        if j == 1:
            dw = (dw + Month[j] + leap(i)) % 7
        else:
            dw = (dw + Month[j]) % 7
        if dw == 0:
            ans += 1
if dw == 0:
    ans -= 1
    #dwで計算しているのは翌月の曜日
print(ans)
