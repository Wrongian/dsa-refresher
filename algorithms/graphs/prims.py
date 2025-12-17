from heapq import heappush, heappop

# each edge in adj list is (v, w)
# cost of min spanning tree
# assume graph is fully connected
def min_cost(adj_list):
  n = len(adj_list)

  # prims
  done = set() 
  pq = []
  # add first and start from 0
  heappush(pq, (0, 0))
  total_cost = 0

  while pq and len(done) < n:
    w, v1  = heappop(pq) 
    if v1 in done: 
      continue

    done.add(v1)
    total_cost += w

    for v, w in adj_list[v1]:
      if v not in done:
        heappush(pq, (w, v))

  # cannot connect all nodes
  if len(done) < n: 
    return -1

  return total_cost
  


