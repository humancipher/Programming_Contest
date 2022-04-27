def pali(a,N):
    B = [set() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i].add(a[i][j])

    output_left,output_right = "",""
    for i in range(N//2):
        C = B[i] & B[N-1-i]
        if len(C) == 0:
            return -1
        else:
            for c in C:
                output_left += c
                output_right = c + output_right
                break
    if N % 2 == 0:
        return output_left + output_right
    else:
        for b in B[N//2]:
            return output_left + b + output_right

def main():
    N = int(input())
    a = [input() for _ in range(N)]

    print(pali(a,N))

if __name__ == "__main__":
    main()
