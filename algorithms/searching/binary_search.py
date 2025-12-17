def mystery_function(n):
  return n > 50

# find first number to the left of func
def binary_search_func(low, high, func):
  left = low
  right = high

  while right >= left:
    # python its fine, other languages prevent overflow
    mid = left + (right - left) // 2

    # cutoff point to the left of mid
    if func(mid):
      right = mid - 1
    # cutoff point to the right of mid
    else:
      left = mid + 1
    
  return left

# returns 51
print(binary_search_func(0, 10000, mystery_function))

def binary_search_sorted_arr(arr, val):
  left = 0
  right = len(arr) - 1

  while right >= left:
    mid = left + (right - left) // 2

    # val in right half
    if val > arr[mid]: 
      left = mid + 1
    # val in left half
    elif val < arr[mid]:
      right = mid - 1
    else:
      # present in array
      return True

  # not present in array
  return False

# first 50 multiple of 5s, in sorted form
sorted_arr = [5*i for i in range(50)]

# True
print(binary_search_sorted_arr(sorted_arr, 60))

# False
print(binary_search_sorted_arr(sorted_arr, 79))


# todo: use bisect in python