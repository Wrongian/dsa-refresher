# number of nodes(can be represented via indexes to be used later)
n = 100

# dont need all of these
parents = [i for i in range(len(n))]
sizes = [1 for i in range(len(n))]
heights = [0 for i in range(len(n))]

# finds uppermost parent of v
def find(v):
  # path compression
  if parents[v] != v:
    parents[v] = find(parents[v])
  return parents[v]

# Returns true if can union, returns false if cannot
def union(v1, v2):
  p1, p2 = find(v1), find(v2)

  # Already have the same parent
  if p1 == p2:
    return False 
  
  # park smaller tree under larger one so height does not increase
  if heights[p1] > heights[p2]:
    parents[p2] = p1
    sizes[p1] += sizes[p2]
  elif heights[p2] > heights[p1]:
    parents[p1] = p2
    sizes[p2] += sizes[p1]
  else:
    # must increase height as both same height
    parents[p1] = p2
    heights[p2] += 1
    sizes[p2] += sizes[p1]

  return True

