import math

n = int(input())

def Prime(n):
    List = [1 for _ in range(n+1)]
    List[0],List[1] = 0,0
    P_List_tmp = [2]
    for i in range(3,n+1):
        flag = 0
        for j in range(len(P_List_tmp)):
            if i % P_List_tmp[j] == 0:
                flag = 1
                List[i] = 0
        if List[i] == 1:
            P_List_tmp.append(i)
    P_List = []
    for i in range(n+1):
        if List[i] == 1:
            P_List.append(i)
    return P_List

def fact(n):
    P_List = Prime(int(math.sqrt(n)))
    Ans = []
    for i in range(len(P_List)):
        if n % P_List[i] == 0:
            while n % P_List[i] == 0:
                n //= P_List[i]
                Ans.append(P_List[i])
    if n != 1:
        Ans.append(n)
    return Ans

print(str(n)+":",end="")
Ans = fact(n)
for i in range(len(Ans)):
    print(" "+str(Ans[i]),end="")
print()

#備考：素数のリスト(sqrt(n)まで)を作ってそれでnを割ったが,
#実際には素数のリストを作らずに2から小さい方から割ってよしだった.
#合成数で割る可能性はより小さい素数で既に割り切って消えているから
