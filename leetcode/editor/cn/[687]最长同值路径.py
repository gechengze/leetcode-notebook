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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.left.val == node.val:
                left1 = left + 1
            else:
                left1 = 0
            if node.right and node.right.val == node.val:
                right1 = right + 1
            else:
                right1 = 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)

        dfs(root)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
