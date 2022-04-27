def judge(N):
    cnt = 0
    while N % 2 == 0:
        N //= 2
        cnt += 1
        if cnt >= 2:
            return "Even"
    if cnt == 0:
        return "Odd"
    if cnt == 1:
        return "Same"

def main():
    T = int(input())
    Ans = []
    for _ in range(T):
        n = int(input())
        Ans.append(judge(n))
    for i in range(T):
        print(Ans[i])

if __name__ == "__main__":
    main()
