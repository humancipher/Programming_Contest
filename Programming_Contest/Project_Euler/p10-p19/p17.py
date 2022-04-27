N = 1000

Al_digit1 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
#Al_digit1[i]:数字i(0<=i<=19)の英語での文字数
Al_digit2 = [0,0,6,6,5,5,5,7,6,6]
#Al_digit2[i]:数字iの2桁目で使われる文字数(10<=i<=19は変則的なのでdigit1で処理)
Al_digit3 = [0,13,13,15,14,14,13,15,15,14]
#Al_digit3[i]:数字iの3桁目で使われる文字数

def counter(n,Al_digit1,Al_digit2,Al_digit3):
    if n == 1000:
        return 11
    else:
        d1,d2,d3 = 0,0,0
        d3 = n // 100
        n %= 100
        if n >= 20:
            d2 = n // 10
            d1 = n % 10
        else:
            d1 = n
        if d3 != 0 and d2 == 0 and d1 == 0:
            #andの3文字がいらない
            return Al_digit3[d3] + Al_digit2[d2] + Al_digit1[d1] -3
        else:
            return Al_digit3[d3] + Al_digit2[d2] + Al_digit1[d1]

ans = 0
for i in range(1,N+1):
    ans += counter(i,Al_digit1,Al_digit2,Al_digit3)
print(ans)
