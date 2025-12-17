# returns all possible subsets from elements
# assume no duplicate elements
def subsets(elements):
  # base case
  ans = [[]]

  def dfs(i, arr):
    for j in range(i, len(elements)):
      new_arr = arr.copy()
      new_arr.append(elements[j])
      ans.append(new_arr.copy())
      dfs(j + 1, new_arr)
  
  dfs(0, [])

  return ans



