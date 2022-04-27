S = input()
Edit = []
for i in range(len(S)):
    if S[i] == "0":
        Edit.append("0")
    if S[i] == "1":
        Edit.append("1")
    if S[i] == "B" and len(Edit) > 0:
        Edit.pop()
print("".join(Edit))
