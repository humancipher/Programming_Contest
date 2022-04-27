A = input().split()

def Revpol(A):
    S = [] #スタック
    for i in range(len(A)):
        if A[i] != '+' and A[i] != '-' and A[i] != '*':
            S.append(int(A[i]))
        elif len(S)>=2:
            if A[i] == '+':
                tmp = S[len(S)-2] + S[len(S)-1]
                S.pop()
                S.pop()
                S.append(tmp)
            elif A[i] == '-':
                tmp = S[len(S)-2] - S[len(S)-1]
                S.pop()
                S.pop()
                S.append(tmp)
            elif A[i] == '*':
                tmp = S[len(S)-2] * S[len(S)-1]
                S.pop()
                S.pop()
                S.append(tmp)
        else:
            print("error1")
            break
    if len(S) == 1:
        print(S[0])
    else:
        print("error2")

Revpol(A)
