class Node:
  def __init__(self, x = None, next = None):
    self.val = x
    self.next = next

def hasCycle(head):
  # slow and fast pointers
  slow = head
  fast = head

  parity = False

  while fast:
    # always update fast pointer
    fast = fast.next

    # update slow pointer every other iteration
    if parity: 
      slow = slow.next
      parity = False
    else:
      parity = True
    
    # check if both pointers meet
    if slow == fast:
      return True

  return False

    

