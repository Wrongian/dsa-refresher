from heapq import heappop, heappush
# k is the starting node index, n is the number of vertices
def min_dist(adj_list, n, k):
  pq = [(0, k - 1)] 
  visited = set()

  while pq and len(visited) != n:
    dist, u = heappop(pq) 

    if u in visited:
      continue
    visited.add(u) 

    for v, w in adj_list[u]:
      if v in visited:
        continue
      
      heappush(pq, (w + dist, v))
  
  if len(visited) < n:
    return -1
  
  # popped last is longest shortest dist from source to any node in the graph
  return dist

    
    


