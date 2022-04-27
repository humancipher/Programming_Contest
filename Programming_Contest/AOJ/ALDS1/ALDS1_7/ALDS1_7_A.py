class Node:
    def __init__(self):
        self.parent_id = -1
        self.depth = 0
        self.children = []

def calc_depth(node_id, arg_depth):
    nodes[node_id].depth = arg_depth
    for child in nodes[node_id].children:
        calc_depth(child, arg_depth+1)

V = int(input())
global nodes
nodes = []
#予めV個のノードを準備
for loop in range(V):
    node = Node()
    nodes.append(node)

#親子関係を取得
for loop in range(V):
    table = list(map(int,input().split()))
    node_id = table[0]
    num = table[1]
    for i in range(num):
        child_id = table[2+i]
        nodes[node_id].children.append(child_id)
        nodes[child_id].parent_id = node_id

#根を探して深さを計算
for i in range(V):
    if nodes[i].parent_id == -1:
        calc_depth(i,0)
        break

for i in range(V):
    print("node %d: parent = %d, depth = %d, "%(i, nodes[i].parent_id, nodes[i].depth),end="")

    if nodes[i].parent_id == -1:
        print("root,",end = "")
    else:
        if len(nodes[i].children) == 0:
            print("leaf,",end="")
        else:
            print("internal node,",end="")

    print(" [",end="")
    print(', '.join(map(str,nodes[i].children)),end="")
    print("]")
