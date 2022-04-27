def pad(S,N):
    return "0" * (N-len(S)) + S

def match(S):
    K = min(3,len(S))
    P = set()

    for i in range(1,K+1):
        for j in range(len(S)-i+1):
            P.add(S[j:j+i])

    P_aster = set()
    for p in P:
        l = len(p)
        for i in range(2**l):
            b = pad(bin(i)[2:],l)
            p_aster = ""
            for j in range(l):
                if b[j] == "0":
                    p_aster += "."
                else:
                    p_aster += p[j]
            P_aster.add(p_aster)

    return len(P_aster)

def main():
    S = input()

    print(match(S))

if __name__ == "__main__":
    main()
