def judge(n):
    m = oct(n)
    if "7" not in m:
        return True
    else:
        return False

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        n = str(i)
        if "7" not in n and judge(i):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
