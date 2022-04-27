from heapq import heappush,heappop,heapify
"""
TPS_sort():トポロジカルソートを行い、かつソート結果が辞書順最小のものを計算する関数
#G[i]:頂点iから出ていく先の頂点の集合
GF[i]:頂点iに入る頂点の集合
Used[i]:頂点iが訪問済かどうか
In0:入次数==0の頂点を扱う優先度付きキュー
n:頂点数
アルゴリズム：
まず空のリストSを用意する
入次数==0の頂点がなくなるまで以下を繰り返す
　入次数==0の頂点で番号が最小の頂点uをSにいれる
　頂点uから出る辺を全て削除する(その結果入次数==0になる頂点があったらそれをIn0に加える)
これで全部の頂点がSに入ったらトポロジカルソート成功
入らない頂点があったらトポロジカルソート失敗
"""
def TPS_dictsort(G,GF,Used,In0,n):
    S = []
    while len(In0) > 0:
        now = heappop(In0)
        Used[now] = True
        S.append(now)
        for nxt in G[now]:
            if not Used[nxt]:
                GF[nxt].discard(now)
                if len(GF[nxt]) == 0:
                    heappush(In0,nxt)
    return S