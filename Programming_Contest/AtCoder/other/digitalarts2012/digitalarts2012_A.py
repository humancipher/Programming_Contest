def judge(s,t):
    for i in range(len(s)):
        if s[i] != t[i] and t[i] != "*":
            return False
    return True

def solve(S,N,T):
    for i in range(len(S)):
        for j in range(len(T)):
            if len(S[i]) == len(T[j]):
                if judge(S[i],T[j]):
                    S[i] = "*" * len(S[i])
    return " ".join(S)

def main():
    S = list(input().split())
    N = int(input())
    T = [input() for _ in range(N)]
    print(solve(S,N,T))

if __name__ == "__main__":
    main()
