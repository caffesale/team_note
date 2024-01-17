class Solution:
  def reverseList(self, head):
    return self.helper(head)
  
  def helper(self, node, prev=None):
    if not node:
      return prev
    next = node.next
    node.next = prev
    return self.helper(next, node)
  

  # iterative
  # prev = None
  # while head:
  #   curr = head
  #   head = head.next
  #   curr.next= prev
  #   prev = curr
  # return prev