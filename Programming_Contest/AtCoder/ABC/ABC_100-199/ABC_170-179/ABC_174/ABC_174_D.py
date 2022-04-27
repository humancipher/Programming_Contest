def solve(C,N):
    W,R = [],[]
    for i in range(N):
        if C[i] == "W":
            W.append(i)
        else:
            R.append(i)

    W.sort(reverse = True)
    cnt = 0

    while True:
        if len(W) > 0 and len(R) > 0:
            if W[-1] < R[-1]:
                cnt += 1
                W.pop()
                R.pop()
            else:
                break
        else:
            break

    return cnt

def main():
    N = int(input())
    C = input()

    ans = solve(C,N)
    print(ans)

if __name__ == "__main__":
    main()
