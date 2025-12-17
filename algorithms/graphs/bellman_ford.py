# let k be the source and n be the number of vertices
def lowest_dist(edges, n: int, k: int):
  dists = [float('inf') for _ in range(n)] 
  dists[k] = 0

  for _ in range(n):
    for u, v, w in edges:
      dists[v] = min(dists[u] + w, dists[v])

  if max(dists) == float("inf"): 
    return - 1

  return max(dists)
    

    

