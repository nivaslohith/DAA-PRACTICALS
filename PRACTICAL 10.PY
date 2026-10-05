def find(parent, i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot == yroot:
        return False

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

    return True

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(vertices))
    rank = [0] * vertices
    mst = []
    cost = 0

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            cost += weight

        if len(mst) == vertices - 1:
            break

    return mst, cost

vertices = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, cost = kruskal(vertices, edges)

print("Edges in MST:")
for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("Total cost:", cost)