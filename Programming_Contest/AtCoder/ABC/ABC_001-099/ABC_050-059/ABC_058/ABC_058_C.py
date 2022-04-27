def solve(S,N):
    C = [[0] * 26 for _ in range(N)] #C[i][j]:S[i]でのj番目のアルファベットの登場数
    for i in range(N):
        for j in range(len(S[i])):
            pt = ord(S[i][j]) - 97 #"a"が97
            C[i][pt] += 1
    
    ans = ""
    for j in range(26):
        tmp = 100
        for i in range(N):
            tmp = min(tmp,C[i][j])
        ans += (chr(97+j) * tmp)
    return ans

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(solve(S,N))

if __name__ == "__main__":
    main()
