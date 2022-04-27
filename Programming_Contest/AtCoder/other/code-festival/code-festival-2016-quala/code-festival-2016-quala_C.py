def solve(S,K):
    for i in range(len(S)-1):
        if S[i] == "a":
            continue
        else:
            if ord("z") - ord(S[i]) < K:
                K -= ord("z") - ord(S[i]) + 1
                S[i] = "a"
            else:
                continue
    S[-1] = chr(97+((ord(S[-1]) - ord("a")) + K % 26) % 26)
    return "".join(S)

def main():
    S = list(input())
    K = int(input())
    print(solve(S,K))

if __name__ == "__main__":
    main()
