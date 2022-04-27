from collections import Counter

def judge(AB,CD,N,M,K,bit):
    Sara = set()
    for i in range(K):
        if bit[i] == "1":
            Sara.add(CD[i][0])
        else:
            Sara.add(CD[i][1])
    ans = 0
    for i in range(M):
        if AB[i][0] in Sara and AB[i][1] in Sara:
            ans += 1
    return ans

def solve(AB,CD,N,M,K):
    ans = 0
    for bit in range(2**K):
        b = bin(bit)[2:]
        b = "0" * (K-len(b)) + b
        ans = max(ans,judge(AB,CD,N,M,K,b))
    return ans

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int,input().split())) for _ in range(K)]

    print(solve(AB,CD,N,M,K))

if __name__ == "__main__":
    main()
