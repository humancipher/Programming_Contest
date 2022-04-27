"""
Preorder
 3 4 0 1 2
Inorder
 4 3 1 0 2
Postorder
 4 1 2 0 3
"""
N = int(input())
Preorder = list(map(int,input().split()))
Inorder = list(map(int,input().split()))

Postorder = [-1 for _ in range(N)]

def L_search(List,key):
    for i in range(len(List)):
        if key == List[i]:
            return i
    return None

pt,pt_l_l,pt_l_r,pr_r_l,pt_r_r = 0,0,0,0,0
#root,左部分木,右部分木
while pt < N:
    pt_l = L_search(Inorder,Preorder[pt])-1
#途中
