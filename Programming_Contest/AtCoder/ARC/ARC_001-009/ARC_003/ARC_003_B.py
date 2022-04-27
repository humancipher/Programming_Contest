def rev(S):
    S = list(S)
    for i in range(len(S)//2):
        S[i],S[len(S)-i-1] = S[len(S)-i-1],S[i]
    S = "".join(S)
    return S

def main():
    N = int(input())
    L = [rev(input()) for _ in range(N)]
    L.sort()
    for i in range(N):
        print(rev(L[i]))

if __name__ == "__main__":
    main()
