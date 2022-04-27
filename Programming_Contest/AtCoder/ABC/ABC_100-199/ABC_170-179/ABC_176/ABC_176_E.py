def solve(B,H,W):
    tate = [0 for _ in range(H)]
    yoko = [0 for _ in range(W)]

    for b in B:
        tate[b[0]-1] += 1
        yoko[b[1]-1] += 1

    tate_max_kouho,yoko_max_kouho = set(),set()
    tate_max,yoko_max = 0,0
    for i in range(H):
        if tate_max == tate[i]:
            tate_max_kouho.add(i)
        elif tate_max < tate[i]:
            tate_max = tate[i]
            tate_max_kouho.clear()
            tate_max_kouho.add(i)

    for j in range(W):
        if yoko_max == yoko[j]:
            yoko_max_kouho.add(j)
        elif yoko_max < yoko[j]:
            yoko_max = yoko[j]
            yoko_max_kouho.clear()
            yoko_max_kouho.add(j)

    C = set() #置かれている爆破物のうち爆破地点候補にはいっている爆破物
    for b in B:
        if (b[0]-1) in tate_max_kouho and (b[1]-1) in yoko_max_kouho:
            C.add(b)

    if len(tate_max_kouho) * len(yoko_max_kouho) > len(C):
        return tate_max + yoko_max
    else:
        return tate_max + yoko_max - 1

def main():
    H,W,M = map(int,input().split())
    B = set([tuple(map(int,input().split())) for _ in range(M)])

    print(solve(B,H,W))

if __name__ == "__main__":
    main()
