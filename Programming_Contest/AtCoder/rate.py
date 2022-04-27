def Rate(n): #最新n回の影響度
    now = 0
    for i in range(n):
        now += 0.9**(i)
    past = (0.9**n)*10
    return (now,past)

n = 40
path = 'rate.txt'
with open(path,'wt') as f:
    for i in range(1,n+1):
        f.write(str(i)+"回目: now : past = "+str(Rate(i)[0])+" : "+str(Rate(i)[1]))
        f.write("\n")
        f.write(str(i)+"回目: now / past = "+str(Rate(i)[0]/Rate(i)[1]))
        f.write("\n\n")
