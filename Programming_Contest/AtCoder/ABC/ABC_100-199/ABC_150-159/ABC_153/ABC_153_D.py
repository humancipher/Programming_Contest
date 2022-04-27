H = int(input())

def Attack(H):
    cnt = 0
    if H == 1:
        return 1
    else:
        return (2*Attack(H//2)+1)

print(Attack(H))
