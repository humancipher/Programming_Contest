N = int(input())
S = input()

half = N // 2
T1, T2 = S[:half], S[half:]
if T1 == T2:
    print('Yes')
else:
    print('No')
