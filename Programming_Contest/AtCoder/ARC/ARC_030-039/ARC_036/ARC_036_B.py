def mt(h):
    sp_L = []
    for i in range(len(h)-2):
        if h[i] > h[i+1] and h[i+1] < h[i+2]:
            sp_L.append(i+1)
    if len(sp_L) > 0:
        pt = sp_L[len(sp_L)//2]
        h1,h2 = h[:pt+1],h[pt:]
        return max(mt(h1),mt(h2))
    else:
        return len(h)

def main():
    N = int(input())
    h = []
    for i in range(N):
        h.append(int(input()))

    ans = mt(h)
    print(ans)

if __name__ == "__main__":
    main()
