x = input()
if "." in x:
    f = x.find(".")
    print(x[:f])
else:
    print(x)
