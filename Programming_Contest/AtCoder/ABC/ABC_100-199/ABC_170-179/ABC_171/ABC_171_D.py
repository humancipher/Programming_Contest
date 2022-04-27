def solve(A,N,Q,BC):
    A_dict = {}
    for a in A:
        if a in A_dict:
            A_dict[a] += 1
        else:
            A_dict[a] = 1

    ans_list = [sum(A)]
    for b,c in BC:
        diff = 0
        if b in A_dict:
            diff += (c-b) * A_dict[b]
            if c in A_dict:
                A_dict[c] += A_dict[b]
            else:
                A_dict[c] = A_dict[b]
            A_dict.pop(b)
        ans_list.append(ans_list[-1] + diff)

    return ans_list[1:]

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]

    ans = solve(A,N,Q,BC)
    for i in range(Q):
        print(ans[i])

if __name__ == "__main__":
    main()
