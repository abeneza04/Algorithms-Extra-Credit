class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

def kruskal(n, edges):
    edges.sort() 
    ds = DisjointSet(n)
    mst = []
    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
    return mst


edges = [
    (1, 0, 1),
    (3, 0, 2),
    (3, 1, 2),
    (6, 1, 3),
    (4, 2, 3)
]
n = 4  

mst = kruskal(n, edges)
print(mst)