INF = 10**20

def dfs(x,ans,diff):
    if ans >= x:
        return ans
    elif ans < 0:
        return INF
    else:
        if 0 < int(str(ans)[0]) - diff and int(str(ans)[0]) - diff < 10:
            if ans == 0 and diff == 0:
                return INF
            elif ans == 0:
                ans = abs(diff) * 10
            else:
                ans += (int(str(ans)[0]) - diff) * 10**(len(str(ans)))
            return dfs(x,ans,diff)
        else:
            return INF

def main():
    x = int(input())
    ans = INF
    for i in range(10):
        for j in range(-9,10):
            ans = min(ans,dfs(x,i,j))
    print(ans)

if __name__ == "__main__":
    main()
