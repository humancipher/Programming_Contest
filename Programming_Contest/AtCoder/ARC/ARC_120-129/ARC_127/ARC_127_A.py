n = int(input())
ans = 0
burst1 = "1"

while int(burst1) <= n:
    pad = ""
    tmp = 0
    while True:
        if int(burst1 + pad) < n:
            if pad != "":
                ans += int(pad) + 1
            else:
                ans += 1
            pad += "9"
        else:
            if pad != "":
                ans += max(0,(n - int(burst1 + "0" * len(pad)) + 1))
            else:
                tmp += 1
                ans += 1
            break
    burst1 += "1"
print(ans)
