N = input()

ans = "No"
for i in range(3):
    if N[i] == "7":
        ans = "Yes"
        print(ans)
        break

if ans == "No":
    print(ans)
