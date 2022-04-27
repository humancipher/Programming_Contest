s = input()

judge1 = len(s) % 2 == 0
judge2 = s[0] == s[len(s)-1]
if judge1 ^ judge2:
    print("Second")
else:
    print("First")