def doble(S):
    N = len(S)
    for i in reversed(range(N)):
        S += S[i]
    return S

def analysis(S):
    stk,spl = [],False
    for i in range(len(S)):
        if S[i] == "(":
            stk.append(i)
        if S[i] == ")":
            p,q = stk.pop(),i
            spl = True
            break
    if spl:
        S_left,S_mid,S_right = S[:p],S[p+1:q],S[q+1:]
        return analysis(S_left + doble(S_mid) + S_right)
    else:
        return S

def main():
    S = input()

    ans = analysis(S)
    print(ans)

if __name__ == "__main__":
    main()
