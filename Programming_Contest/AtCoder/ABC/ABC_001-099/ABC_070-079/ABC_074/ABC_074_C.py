def cal(A,B,C,D,E,F):
    div = [0 for _ in range(4)]
    div[0] = F // (100 * A)
    div[1] = F // (100 * B)
    if B % A == 0:
        div[1] = 0
    div[2] = (F * E) // ((100 + E) * C)
    div[3] = (F * E) // ((100 + E) * D)
    if D % C == 0:
        div[3] = 0

    concent,concent_max = -1.0,[0,0]
    for i2 in range(div[1]+1):
        for i1 in range(div[0]+1):
            for j2 in range(div[3]+1):
                for j1 in range(div[2]+1):
                    if 100 * (A * i1 + B * i2) + (C * j1 + D * j2) <= F \
                    and (C * j1 + D * j2) <= E * (A * i1 + B * i2) \
                    and ((i1 != 0) or (i2 != 0)):
                        if concent < (C * j1 + D * j2) / (A * i1 + B * i2):
                            concent = (C * j1 + D * j2) / (A * i1 + B * i2)
                            concent_max = [C * j1 + D * j2 , (A * i1 + B * i2) * 100]
                    else:
                        break

    return concent_max

def main():
    A,B,C,D,E,F = map(int,input().split())

    concent_max = cal(A,B,C,D,E,F)
    print(concent_max[0] + concent_max[1],concent_max[0])

if __name__ == "__main__":
    main()
