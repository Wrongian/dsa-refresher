def find_k_smallest(nums, k):
  
  # pivots the range [left, right] around the pivot of p_index
  # returns the order of the pivot
  # assume rightmost element is pivot
  def partition(left, right): 
    pivot = nums[right]

    order = left

    for i in range(left, right):
      if nums[i] <= pivot:
        # increment left, one more element <= pivot
        nums[order], nums[i] = nums[i], nums[order]
        order += 1
        
    # move pivot in order
    nums[order], nums[right] = nums[right], nums[order]

    # return pivot index
    return order

  left = 0
  right = len(nums) - 1

  while True:
    p_index = partition(left, right) 
    if p_index == k:
      return nums[p_index]
    elif p_index < k:
      left = p_index + 1 
    else:
      right = p_index - 1
  


