"""
Problem: given a wighted and undirect graph. This algorithm needs to find a subset of edges that has all the vertices
connected. Has the minimum total edge weight.
Result is in the README
"""
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # number of vertices
        self.edges = []    # list to store edges in the form (u, v, weight)

    def add_edge(self, u, v, w):
        #Add an edge to the graph
        self.edges.append((u, v, w))

    def find(self, parent, i):
        #Find set of element i with path compression.
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        #Union two sets by rank
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self):
        #Construct MST using Kruskal's algorithm.
        # Sort edges by weight
        self.edges.sort(key=lambda edge: edge[2])

        parent = [i for i in range(self.V)]  # parent of each vertex
        rank = [0] * self.V                  # rank for union by rank
        mst = []                       

        for u, v, w in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If adding this edge doesn't create a cycle
            if x != y:
                mst.append((u, v, w))
                self.union(parent, rank, x, y)

            # Stop if MST has V-1 edges
            if len(mst) == self.V - 1:
                break
        total_weight = 0
        print("Edges in the constructed MST:")
        for u, v, w in mst:
            total_weight += w
            print(f"{u} -- {v} == {w}")
        print("Total weight of MST:", total_weight)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()