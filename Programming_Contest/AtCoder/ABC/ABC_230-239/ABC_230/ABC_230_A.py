n = int(input())
if n >= 42:
    n += 1
n = "0"*(3-len(str(n)))+str(n)
print("AGC"+str(n))