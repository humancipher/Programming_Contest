def min_dist(D):
    N = len(D)
    if N == 1:
        return D[0]
    else:
        max_d,max_d_i = 0,0
        for i in range(N):
            if D[i] > max_d:
                max_d,max_d_i = D[i],i
        output = max(2*max_d - sum(D),0)
        return output

def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]

    max_d,min_d = sum(D),min_dist(D)
    print(max_d)
    print(min_d)

if __name__ == "__main__":
    main()
