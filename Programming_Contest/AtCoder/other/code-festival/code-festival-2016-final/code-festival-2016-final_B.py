def solve(N):
    ans_list = []
    for n in range(1,N+1):
        ans_list.append(n)
        if n * (n+1) // 2 == N:
            return ans_list
        elif n * (n+1) // 2 > N:
            ans_list.remove(sum(ans_list) - N)
            return ans_list
        else:
            continue

def main():
    N = int(input())

    ans = solve(N)
    for i in range(len(ans)):
        print(ans[i])

if __name__ == "__main__":
    main()
