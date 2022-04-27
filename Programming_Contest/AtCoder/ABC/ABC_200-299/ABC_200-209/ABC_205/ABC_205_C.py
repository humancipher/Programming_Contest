a,b,c = map(int,input().split())

if a == b:
    print("=")
else:
    if c % 2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) == abs(b):
            print("=")
        else:
            print("<")
    else:
        if a == 0 and b == 0:
            print("=")
        elif abs(a) == abs(b):
            if a * b < 0:
                if a < 0:
                    print("<")
                else:
                    print(">")
            elif a * b == 0:
                if a == 0:
                    if b < 0:
                        print(">")
                    else:
                        print("<")
                elif b == 0:
                    if a < 0:
                        print("<")
                    else:
                        print(">")
            else:
                print("=")
        elif abs(a) > abs(b):
            if a > 0:
                print(">")
            else:
                print("<")
        else:
            if b > 0:
                print("<")
            else:
                print(">")

