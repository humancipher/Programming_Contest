X = input()
ans = "Weak"
for i in range(3):
    if not ((int(X[i]) + 1) % 10 == int(X[i+1]) % 10):
        ans = "Strong"
if X[0] == X[1] == X[2] == X[3]:
    ans = "Weak"
print(ans)