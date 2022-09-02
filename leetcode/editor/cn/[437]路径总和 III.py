from typing import Optional
from playground import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def cal_path_sum(root, sum_):
            if not root:
                return 0
            sum_ -= root.val
            temp = 1 if sum_ == 0 else 0
            return temp + cal_path_sum(root.left, sum_) + cal_path_sum(root.right, sum_)

        return cal_path_sum(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum )
# leetcode submit region end(Prohibit modification and deletion)
