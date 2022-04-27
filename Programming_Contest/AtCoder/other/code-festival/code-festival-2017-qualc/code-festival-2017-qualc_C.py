def solve(s):
    left,right = 0,len(s)-1
    ans = 0
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] == "x" and s[right] != "x":
            ans += 1
            left += 1
        elif s[left] != "x" and s[right] == "x":
            ans += 1
            right -= 1
        else:
            ans = -1
            break

    return ans

def main():
    s = input()
    print(solve(s))

if __name__ == "__main__":
    main()
