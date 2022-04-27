def solve(R,N):
    ans = N
    fugo = ""
    for i in range(N-1):
        if R[i] < R[i+1]:
            now = "plus"
        elif R[i] > R[i+1]:
            now = "minus"
        else:
            now = "zero"
        if now == "zero":
            ans -= 1
        else:
            if fugo != "":
                if not((fugo,now) == ("plus","minus") or (fugo,now) == ("minus","plus")):
                    ans -= 1
            fugo = now
    if ans >= 3:
        return ans
    else:
        return 0

def main():
    N = int(input())
    R = list(map(int,input().split()))
    print(solve(R,N))

if __name__ == "__main__":
    main()
