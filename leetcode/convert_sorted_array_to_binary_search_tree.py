# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None,right=None):
#       self.val = val
#       self.left = left
#       self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        list_len = len(nums)
        if not list_len:
            return None
        mid_val = list_len // 2
        return TreeNode(nums[mid_val], self.sortedArrayToBST(nums[:mid_val], self.sortedArrayToBST(nums[mid_val + 1]))
