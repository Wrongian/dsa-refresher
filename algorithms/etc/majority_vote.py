# assume len(nums) >= 1
def majority_element(nums):
  # start with first element
  count = 1  
  ele = nums[0]

  for i in range(1, len(nums)):
    num = nums[i]

    if ele != num:
      count -= 1
    else:
      count += 1

    if count == 0:
      ele = num
      count = 1

  return ele