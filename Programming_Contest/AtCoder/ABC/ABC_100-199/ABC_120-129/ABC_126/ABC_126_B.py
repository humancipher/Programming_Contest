S = input()
L,R = int(S[:2]),int(S[2:])
if 1 <= L <= 12 and 1 <= R <= 12:
    print("AMBIGUOUS")
elif 1 <= L <= 12:
    print("MMYY")
elif 1 <= R <= 12:
    print("YYMM")
else:
    print("NA")
