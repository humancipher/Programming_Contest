from itertools import accumulate
from sys import stdin
input = stdin.readline

def main():
    limit = 5000
    n,k = map(int,input().split())
    Data = [[0] * (limit+1) for _ in range(limit+1)]
    for _ in range(n):
        a,b = map(int,input().split())
        Data[a][b] += 1
    for i in range(limit+1):
        Data[i] = list(accumulate(Data[i]))
    for i in range(limit):
        for j in range(limit+1):
            Data[i+1][j] += Data[i][j]
    ans = 0
    for i in range(limit-k):
        for j in range(limit-k):
            tmp = Data[i+k+1][j+k+1] - Data[i+k+1][j] - Data[i][j+k+1] + Data[i][j]
            ans = max(tmp,ans)
    print(ans)

if __name__ == "__main__":
    main()
