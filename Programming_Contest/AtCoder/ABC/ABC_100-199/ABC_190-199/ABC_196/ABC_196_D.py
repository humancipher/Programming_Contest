def dfs(T,H,W,A,pt):
    #T[i]:i枚目の長畳の(左上の座標(スカラー表現),向き(0なら縦置き、1なら横置き))
    #T:長畳を置いてあるマス（スカラー表現）の集合
    #pt:現在畳を置こうとしている座標のスカラー表現
    if len(T) == 2*A:
        return 1
    elif pt == H*W:
        return 0
    else:
        if pt % W != W-1 and pt not in T and pt+1 not in T: #長畳横置き
            pat1 = dfs(T | set([pt,pt+1]),H,W,A,pt+1)
        else:
            pat1 = 0
        if pt // W != H-1 and pt not in T and pt+W not in T: #長畳縦置き
            pat2 = dfs(T | set([pt,pt+W]),H,W,A,pt+1)
        else:
            pat2 = 0
        pat3 = dfs(T,H,W,A,pt+1)
        return pat1 + pat2 + pat3

def main():
    H,W,A,B = map(int,input().split())
    print(dfs(set(),H,W,A,0))

if __name__ == "__main__":
    main()
