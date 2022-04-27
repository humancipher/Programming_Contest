N = input()

a = N[0]

def judge(N,a):
    pt = 0
    while pt < len(N):
        if int(N[pt]) < a:
            return False
        elif int(N[pt]) > a:
            return True
        else:
            pt += 1
    return False

ans = ""
if judge(N,int(a)):
    a = str(int(a)+1)
for i in range(len(N)):
    ans += a
print(ans)
