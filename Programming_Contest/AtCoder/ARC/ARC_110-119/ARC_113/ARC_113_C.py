def solve(S,N):
    ans = 0
    bef_alf = "" #直前でbef_alfに書き換えた
    bef_pt = N
    for i in reversed(range(N-2)):
        if S[i] == S[i+1]:
            T = S[i+2:bef_pt]
            tmp = len(T) - T.count(S[i])
            if S[i] != bef_alf:
                tmp += N - bef_pt
            ans += tmp
            bef_alf = S[i]
            bef_pt = i
    return ans

def main():
    S = input()
    print(solve(S,len(S)))

if __name__ == "__main__":
    main()
