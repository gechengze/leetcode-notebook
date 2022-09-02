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
    def __init__(self):
        self.result = int(-1e10)

    def dfs(self, root):
        if not root:
            return 0
        left_result = self.dfs(root.left)
        right_result = self.dfs(root.right)
        self.result = max(self.result, root.val + left_result + right_result)
        max_value = max(root.val + left_result, root.val + right_result)
        return max_value if max_value >= 0 else 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.result

# leetcode submit region end(Prohibit modification and deletion)
