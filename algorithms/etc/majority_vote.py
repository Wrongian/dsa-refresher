# assume len(nums) >= 1
def majority_element(elements):
  # start with first element
  count = 1  
  candidate = elements[0]

  for i in range(1, len(elements)):
    num = elements[i]

    if candidate != num:
      count -= 1
    else:
      count += 1

    if count == 0:
      candidate = num
      count = 1

  count = 0
  for ele in elements:
    if ele == candidate:
      count += 1
  
  if count > len(elements) // 2:
    return candidate
  else:
    # no majority candidate in the list
    return None
