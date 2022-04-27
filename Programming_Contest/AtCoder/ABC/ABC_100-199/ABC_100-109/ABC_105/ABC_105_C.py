def solve(N,digit,ans): #暫定N,digit:見てる桁が偶数なら1,奇数なら-1,暫定解
    if N == 0:
        if ans == "":
            return "0"
        else:
            return ans
    else:
        if N % 2 == 0:
            return solve(N//2,-digit,"0"+ans)
        else:
            return solve((N-digit)//2,-digit,"1"+ans)

def main():
    N = int(input())
    print(solve(N,1,""))

if __name__ == "__main__":
    main()
