INF = 10**9

def solve(RGB):
    ans = INF
    for i in range(3):
        if (RGB[i]-RGB[(i+1)%3])%3 == 0:
            ans = min(ans,max(RGB[i],RGB[(i+1)%3]))
    if ans == INF:
        return -1
    else:
        return ans

def main():
    t = int(input())
    for _ in range(t):
        print(solve(list(map(int,input().split()))))

if __name__ == "__main__":
    main()
