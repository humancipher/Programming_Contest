def judge(S):
    c = 0
    for i in range(5):
        c += S[i].count("#")

    if c == 7:
        return 7
    elif c == 8:
        return 1
    elif c == 9:
        return 4
    elif c == 11:
        #候補:2,3,5
        if S[1][3] == "#" and S[3][3] == "#":
            return 3
        elif S[1][3] == "#":
            return 2
        else:
            return 5
    elif c == 12:
        #候補:0,6,9
        if S[1][3] == ".":
            return 6
        elif S[3][1] == ".":
            return 9
        else:
            return 0
    else:
        return 8

def main():
    N = int(input())
    s = [input() for _ in range(5)]

    T = [[] for _ in range(N)]
    for i in range(N):
        for j in range(5):
            T[i].append(s[j][i*4:i*4+4])

    ans = ""
    for i in range(N):
        ans += str(judge(T[i]))

    print(ans)

if __name__ == "__main__":
    main()
