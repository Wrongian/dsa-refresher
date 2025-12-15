def permute(nums):
  ans = []

  arr = []
  done = set()

  def dfs(): 
    # termination
    if len(arr) == len(nums):
      ans.append(arr.copy())
      return
    
    # propagation
    for num in nums:
      # avoid duplicates
      if num in done:
        continue
      
      # do
      arr.append(num)
      done.add(num)

      dfs()

      # undo
      arr.pop()
      done.remove(num)

  dfs()   
  return ans
  




      
