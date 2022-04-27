def cal(S):
    N = len(S)
    num,cnt = 0,0
    mod = 2019
    rem = [0 for _ in range(mod)]
    for i in range(N):
        num = (num + int(S[N-1-i]) * pow(10,i,mod)) % mod
        rem[num] += 1

    output = rem[0] * (rem[0] + 1) // 2
    for i in range(1,mod):
        output += rem[i] * (rem[i] - 1) // 2

    return output

def main():
    S = input()

    print(cal(S))

if __name__ == "__main__":
    main()
