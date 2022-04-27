def solve(S):
    ans = 0
    ls = len(S)-1
    for i in range(2**ls):
        left,right = 0,ls
        for j in range(ls):
            if 1 << j & i:
                right = j
                ans += int(S[left:right+1])
                left = j+1
        if left <= ls:
            ans += int(S[left:ls+1])
    return ans

def main():
    S = input()
    print(solve(S))

if __name__ == "__main__":
    main()
