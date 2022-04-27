N = 1000

def judge(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

for a in range(1,N//3):
    for b in range(a+1,N//2):
        if judge(a,b,N-a-b):
            ans = a*b*(N-a-b)
            break

print(ans)
