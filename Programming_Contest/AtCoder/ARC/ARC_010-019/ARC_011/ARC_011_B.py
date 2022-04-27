def Dec(W):
    D = [{"z","r"},{"b","c"},{"d","w"},{"t","j"},{"f","q"},\
         {"l","v"},{"s","x"},{"p","m"},{"h","k"},{"n","g"}]

    ans = ""
    for i in range(len(W)):
        big = 0
        if 65 <= ord(W[i]) and ord(W[i]) <= 90:
            big = 1
        for j in range(10):
            if chr(ord(W[i]) + big * 32) in D[j]:
                ans += str(j)

    return ans

def main():
    N = int(input())
    W = list(input().replace(".","").split())

    ans = ""
    for i in range(len(W)):
        dec = Dec(W[i])
        if dec != "":
            ans += (dec+" ")

    if ans != "":
        ans = ans[:len(ans)-1]
    print(ans)

if __name__ == "__main__":
    main()
