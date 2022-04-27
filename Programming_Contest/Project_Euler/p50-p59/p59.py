def dec(C,K):
    lc,lk,pt = len(C),len(K),0
    m = ""
    while pt < lc:
        for i in range(lk):
            ck = C[pt]^K[i]
            if 32 <= ck <= 126:
                m += chr(C[pt]^K[i])
            else:
                return ""
            pt += 1
            if pt >= lc:
                break
    return m

def main():
    path = "./p59_input.txt"

    with open(path) as f:
        C = f.read().split(",")

    for i in range(len(C)):
        C[i] = int(C[i])

    path_w = "./p59_output.txt"

    with open(path_w,mode = "w") as f:
        for k1 in range(97,123):
            for k2 in range(97,123):
                for k3 in range(97,123):
                    K = [k1,k2,k3]
                    m = dec(C,K)
                    if m != "" and " of " in m:
                        f.write(m)
                        f.write("\n\n")
                        M = m

    ans = 0
    for i in range(len(M)):
        ans += ord(M[i])

    print(ans)

if __name__ == "__main__":
    main()
