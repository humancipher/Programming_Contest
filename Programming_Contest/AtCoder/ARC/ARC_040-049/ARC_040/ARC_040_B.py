import sys
input = sys.stdin.readline

def main():
    n,r = map(int,input().split())
    S = list(input().rstrip())
    cnt = 0
    for i in range(n):
        if S[i] == "o":
            cnt += 1
    if cnt == n: #最初から全て塗られている
        print(0)
    else:
        for _ in range(n):
            S.append("o")
        ans,pt = 0,0
        while cnt < n:
            if S[pt] == "o":
                ans += 1
                pt += 1
            else:
                ans += 2
                last = pt
                for j in range(r):
                    if S[pt+j] == ".":
                        S[pt+j] = "o"
                        cnt += 1
                        last = pt+j
                if cnt == n:
                    diff = pt+r-last
                    ans -= diff
                pt += 1
        print(max(1,ans)) #最初の1発で全部塗れて射程が過剰なときにans <= 0になる

if __name__ == "__main__":
    main()