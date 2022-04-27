s = ""
p = [1,10,10**2,10**3,10**4,10**5,10**6]

ans,num = 1,1
while len(s) < p[6]:
    s += str(num)
    num += 1

for i in range(7):
    ans *= int(s[p[i]-1])

print(ans)
