class Solution:
  def merge_to_lists(self, list1, list2):
    if not list1:
      return list2
    if not list2:
      return list1
    if list1.val < list2.val:
      list1.next = self.merge_to_lists(list1.next, list2)
      return list1
    else:
      list2.next = self.merge_to_lists(list1, list2.next)
      return list2