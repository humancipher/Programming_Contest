A,B,C = map(int,input().split())

if ((A == B) and (A != C)) or ((B == C) and (C != A)) or ((C == A) and (C != B)):
    print('Yes')
else:
    print('No')
