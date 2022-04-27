S = input()

def judge(S):
    for i in range(len(S)//2):
        if S[i] != S[len(S)-1-i]:
            return False
    return True

S0 = S[0:(len(S)-1)//2]
S1 = S[(len(S)+3)//2-1:len(S)]

if judge(S) and judge(S0) and judge(S1):
    print("Yes")
else:
    print("No")
