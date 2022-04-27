N,A,B = map(int,input().split())

if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    if A - 1 < N - B:
        B1 = B - A
        coll = (B1 + 1) // 2
        print(B - coll)
    else:
        A1 = A + (N - B) + 1
        coll = (A1 + N) // 2
        print(coll - A)
