from itertools import accumulate

def main():
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    S = [0] * m #S[i]:i番目の区間を捨てて失うスコア
    score = 0
    for _ in range(n):
        l,r,s = map(int,input().split())
        score += s
        S[l-1] += s
        if r < m:
            S[r] -= s
    S = list(accumulate(S))
    print(score - min(S))

if __name__ == "__main__":
    main()
