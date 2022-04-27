#python では駄目だがpypyなら間に合う
N = int(input())
S = input()

def judge(S,A): #A:3桁ｎ数字
    dig,pt = 0,0
    while dig < 3 and pt < N:
        if S[pt] == A[dig]:
            dig += 1
            pt += 1
        else:
            pt += 1
        if dig == 3:
            break

    if dig == 3:
        return True
    else:
        return False

count = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if judge(S,[str(a),str(b),str(c)]):
                count += 1

print(count)
