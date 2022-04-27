def String_kind(S):
    S_kind,S_kind_num,count = set(),{},0
    OP = []
    for i in range(len(S)):
        if S[i] not in S_kind:
            S_kind.add(S[i])
            S_kind_num[S[i]] = count
            count += 1
        OP.append(S_kind_num[S[i]])

    return OP

def main():
    S = input()
    T = input()

    S_kind,T_kind = String_kind(S),String_kind(T)
    if S_kind == T_kind:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
