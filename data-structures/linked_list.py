class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next
    

# reverses a linked list iteratively
def reverse(head):
  node = head 
  last = None
  next_node = None

  while node:
    next_node = node.next

    if last:
      node.next = last
    else: 
      # first node
      node.next = None

    last = node 
    node = next_node 

  return last

 