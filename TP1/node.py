import numpy as np

class Node:
    def __init__(self, table):
        self.table = table

    def getChilds(node):
        for i in range(3):
            for j in range(3):
                if ( node[i][j] == 0 ):
                    return 1
                    
    def genChilds(node): 
        childs = []
        for i in range(3):
            for j in range(3):
                if (node.table[i][j] == 0):
                    if ( i < 2 ):
                        childs.append(Node(node.swap(i,j,1,0))) # estan etiquetados al revez pq python es muy raro manana con el math.py lo sol
                        print("rigth")
                    if ( j < 2 ):
                        childs.append(Node(node.swap(i,j,0,1)))
                        print("up")
                    if ( j > 0 ):
                        childs.append(Node(node.swap(i,j,0,-1)))
                        print("bottom")
                    if ( i > 0 ):
                        childs.append(Node(node.swap(i,j,-1,0)))
                        print("left")
        return childs

    def swap(node, i, j, x, y):
        table = node.table
        print(i,j,x,y)
        table[i][j], table[i+x][j+y] = table[i+x][j+y], table[i][j]
        node.print()
        return table

    def print(node):
        for i in range(3):
            for j in range(3):
                print(node.table[i][j], end= " ")
            print("\n")
        

node = Node([[1,2,3],[4,5,6],[7,8,0]])
node.print()
print("----------------")
aux = node.genChilds()
# for i in range(len(aux)):
    # aux[i].print()