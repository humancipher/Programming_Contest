def solve(S,a,r): #(S,a,r) = (現在の文字列,狙う単一文字,再帰回数)
    if len(set(S)) == 1:
        return r
    else:
        T = ""
        for i in range(len(S)-1):
            if S[i] == a or S[i+1] == a:
                T += a
            else:
                T += S[i+1]
        return solve(T,a,r+1)

def main():
    S = input()
    S_set = set(S)
    
    ans = len(S)
    for al in S_set:
        ans = min(ans,solve(S,al,0))
    print(ans)

if __name__ == "__main__":
    main()
