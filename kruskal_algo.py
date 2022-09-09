# IU1941230087
# RAJAT NANAVATI
# CSE_B

from collections import defaultdict
 
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  
        self.graph = []  
        
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimumCost = 0
        print ("Edges")
        for u, v, weight in result:
            minimumCost += weight
            print("%d  -  %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
 
# IU1941230087
# RAJAT NANAVATI
# CSE_B

g = Graph(7)
g.addEdge(0,1,1)
g.addEdge(0,3,4)
g.addEdge(1,3,6)
g.addEdge(1,4,4)
g.addEdge(1,2,2)
g.addEdge(1,4,4)
g.addEdge(2,4,5)
g.addEdge(2,5,6)
g.addEdge(3,4,3)
g.addEdge(3,6,4)
g.addEdge(4,6,7)
g.addEdge(4,5,8)
g.addEdge(5,6,3)
 
g.KruskalMST()