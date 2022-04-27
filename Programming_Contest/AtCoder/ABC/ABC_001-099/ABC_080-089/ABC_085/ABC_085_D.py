from math import ceil

def attack(ab,N,H):
    cut_max = 0
    for i in range(N):
        cut_max = max(cut_max,ab[i][0])

    throw = [ab[i][1] for i in range(N)]
    throw.sort(reverse = True)
    throw.append(0)

    cnt,pt = 0,0
    while H > 0:
        if throw[pt] > cut_max:
            H -= throw[pt]
            cnt += 1
            pt += 1
        else:
            cnt += (ceil(H/cut_max))
            H = 0

    return cnt

def main():
    N,H = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(N)]

    print(attack(ab,N,H))

if __name__ == "__main__":
    main()
