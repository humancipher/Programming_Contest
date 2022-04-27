ATC = "atcoder"

def solve(S):
    if S > ATC:
        return 0
    else:
        pt = len(S)
        for i in range(len(S)):
            if S[i] != "a":
                pt = i
                break
        if pt == len(S):
            return -1
        else:
            if pt == 0:
                return 0
            else:
                if S[pt] > "t":
                    return pt-1
                else:
                    return pt

def main():
    import sys
    input = sys.stdin.readline
    Ans = []
    t = int(input())
    for _ in range(t):
        S = input().rstrip()
        Ans.append(solve(S))
    for i in range(t):
        print(Ans[i])

if __name__ == "__main__":
    main()
