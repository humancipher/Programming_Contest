m = int(input())

if m < 100:
    ans = "00"
elif m <= 5000:
    ans = m // 100
    if len(str(ans)) == 1:
        ans = "0" + str(ans)
if 6000 <= m <= 30000:
    ans = m // 1000 + 50
if 35000 <= m <= 70000:
    ans = ((m // 1000 - 30) // 5 + 80)
if m > 70000:
    ans = 89
print(ans)
