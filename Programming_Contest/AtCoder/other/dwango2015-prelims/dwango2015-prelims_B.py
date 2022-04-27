def search_25(S):
    OP = []
    for i in range(len(S)-1):
        if S[i] == "2" and S[i+1] == "5":
            OP.append(i)
    return OP

def cont_25(list_25):
    list_25_cont = []
    pt,cont = 0,1
    while pt < len(list_25)-1:
        if list_25[pt]+2 == list_25[pt+1]:
            cont += 1
        else:
            list_25_cont.append(cont)
            cont = 1
        pt += 1
    if len(list_25) > 0:
        list_25_cont.append(cont)
    return list_25_cont

def sum_1_to_n(n):
    return n*(n+1)//2

def main():
    S = input()
    search25 = search_25(S)
    cont25 = cont_25(search25)
    ans = 0
    for i in range(len(cont25)):
        ans += sum_1_to_n(cont25[i])
    print(ans)

if __name__ == "__main__":
    main()
