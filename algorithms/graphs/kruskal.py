# edges is a list of (weight, u, v) tuples, n is the number of vertices
# returns the total weight of the MST, or -1 if the graph is not connected
def kruskals(edges, n):

    edges.sort()
    
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):

        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):

        px, py = find(x), find(y)

        if px == py:
            return False

        elif rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] == rank[py]:
            rank[px] += 1
            parent[py] = px
        else:
            parent[py] = px        
        return True

    res = 0
    count = 0

    for weight, u, v in edges:

        if union(u, v):
            res += weight
            count += 1
            if count == n - 1:
                break

    return res if count == n - 1 else -1
