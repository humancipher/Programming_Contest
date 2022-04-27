N,M = map(int,input().split())
KS = [list(map(int,input().split())) for i in range(M)]
P = list(map(int,input().split()))

def Bit(x,N):
    bit = [0 for _ in range(N)]
    for i in range(N):
        if x - 2**(N-i-1) >= 0:
            bit[i] = 1
            x -= 2**(N-i-1)
    return bit

def judge(a,N):
    bit = Bit(a,N)
    LB= [P[i] for i in range(M)]
    for i in range(N):
        if bit[i] == 1:
            for j in range(M):
                if i+1 in KS[j][1:len(KS[j])]:
                    LB[j] += 1
                    LB[j] %= 2
    if sum(LB) == 0:
        return True
    else:
        return False

count = 0
for i in range(2**N):
    if judge(i,N):
        count += 1
print(count)
