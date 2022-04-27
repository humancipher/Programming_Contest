def solve(L):
    #L[i]:[(i番目のカードの種類,i番目のカードの番号)]
    Big = set(["10","J","Q","K","A"])
    SHDC = {"S":0,"H":1,"D":2,"C":3}
    Hand = [set() for _ in range(4)] #S,H,D,Cの9以上での入手札
    for i in range(len(L)):
        if L[i][1] in Big:
            Hand[SHDC[L[i][0]]].add(L[i][1])
            if len(Hand[SHDC[L[i][0]]]) == 5:
                use = L[i][0] #RFSを揃えるために使うカードの種類
                last = i
                break
    Ans = []
    for i in range(last+1):
        if L[i][0] != use or L[i][1] not in Big:
            Ans.append(L[i][0]+L[i][1])
    return "".join(Ans)

def main():
    S = input()
    S += "_"
    pt = 0
    SHDC = set(["S","H","D","C"])
    L = []
    while pt < len(S)-1:
        if S[pt] in SHDC:
            a = S[pt]
            pt += 1
            if S[pt+1] == "0":
                b = S[pt:pt+2]
                pt += 2
            else:
                b = S[pt]
                pt += 1
            L.append((a,b))
    Ans = solve(L)
    if len(Ans) == 0:
        print(0)
    else:
        print(Ans)

if __name__ =="__main__":
    main()

