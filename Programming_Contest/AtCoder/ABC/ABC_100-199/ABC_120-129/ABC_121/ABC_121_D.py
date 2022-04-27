def xor_sum(a):
    if a == 0 or a == 1:
        return a
    elif a == 2:
        return 3
    elif a == 3:
        return 0
    else:
        b = bin(a)[2:]
        if a % 2 == 0:
            return 2**(len(b)-1) + xor_sum(a % 2**(len(b)-1))
        else:
            return xor_sum(a % 2**(len(b)-1))

def main():
    A,B = map(int,input().split())

    a,b = xor_sum(max(0,A-1)),xor_sum(B)
    print(a ^ b)

if __name__ == "__main__":
    main()
