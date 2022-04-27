def solve(NML):
    for nml in NML:
        nml.sort()
    n_max,m_max,l_max = 0,0,0
    for nml in NML:
        n_max = max(n_max,nml[0])
        m_max = max(m_max,nml[1])
        l_max = max(l_max,nml[2])

    return n_max * m_max * l_max

def main():
    C = int(input())
    NML = [list(map(int,input().split())) for _ in range(C)]

    print(solve(NML))

if __name__ == "__main__":
    main()
