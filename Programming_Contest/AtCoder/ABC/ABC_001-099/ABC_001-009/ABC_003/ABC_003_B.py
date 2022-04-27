def win(S,T):
    joker = set(["a","t","c","o","d","e","r"])
    for i in range(len(S)):
        if S[i] != T[i]:
            if T[i] == "@":
                if S[i] not in joker:
                    return False
            if S[i] == "@":
                if T[i] not in joker:
                    return False
            if S[i] != "@" and T[i] != "@":
                return False
    return True

def main():
    S = input()
    T = input()

    if win(S,T):
        print("You can win")
    else:
        print("You will lose")

if __name__ == "__main__":
    main()
