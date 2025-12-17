# (u, v) in edges means that v depends on u
def find_ordering(n, edges):
  incoming_edges = [0 for _ in range(n)]
  adj_list = [[] for _ in range(n)]

  for u, v in edges:
    incoming_edges[v] += 1
    adj_list[u].append(v)
  
  frontier = [] 

  for i in range(len(incoming_edges)):
    if incoming_edges[i] == 0:
      frontier.append(i)
  
  ordering = []
  while frontier: 
    new_frontier = []

    for u in frontier: 
      for v in adj_list[u]:
        incoming_edges[v] -= 1
        if incoming_edges[v] == 0:
          new_frontier.append(v)
        
      ordering.append(u)

    frontier = new_frontier 

  # if all vertices not included
  if len(ordering) != n:
    return []

  return ordering 


